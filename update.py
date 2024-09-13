import os, bibtexparser
from bs4 import BeautifulSoup

def sort_bib_database(bib_database: list) -> list:
    status_order = ['Concluded', 'Reading', 'Queued', 'Pending', 'Other', 'Archived']
    grouped_data = {status: [] for status in status_order}

    for entry in bib_database.entries:
        status = entry.get('status', 'Pending')
        grouped_data[status if status in status_order else 'Other'].append(entry)

    return [entry for status in status_order for entry in grouped_data[status]]

def get_color(status: str) -> str:
    status_colors = {
        'Concluded': '🔵',
        'Reading': '🟢',
        'Queued': '🟠',
        'Skipped': '⚫️',
    }

    return status_colors.get(status, '🟡')

def main():
    subjects_dir = 'Research Subjects'
    subject_list = os.listdir(subjects_dir)
    for subject in subject_list:
        bib_file = os.path.join(subjects_dir, subject, 'references.bib')
        
        # Read BibTeX file
        with open(bib_file, 'r') as file:
            bib_database = bibtexparser.load(file)

            html_rows = []
            for entry in sort_bib_database(bib_database):
                title = entry.get('title', 'No title')
                author = entry.get('author', 'No author')
                year = entry.get('year', 'No year')
                url = entry.get('url', '')
                url_link = 'Link' if url!='' else ''
                status = entry.get('status', 'Pending')
                comment = entry.get('comment', '')
                color=get_color(status)

                html_rows.append(f"""
                    <tr>
                        <td>{title}</td>
                        <td>{author}</td>
                        <td>{year}</td>
                        <td><a href='{url}' target='_blank'>{url_link}</a></td>
                        <td>{color}{status}</td>
                        <td>{comment}</td>
                    </tr>
                """)

        html_table = ''.join(html_rows)

        html_code = f"""
            <!DOCTYPE html>
            <html lang='en'>
            <head>
                <meta charset='UTF-8'>
            </head>
            <body>
                <table id='example' class='display' border='1'>
                    <thead>
                        <tr>
                            <th>Title</th>
                            <th>Author</th>
                            <th>Year</th>
                            <th>Source</th>
                            <th>Status</th>
                            <th>Comment</th>
                        </tr>
                    </thead>
                    <tbody>
                        {html_table}
                    </tbody>
                </table>
            </body>
            </html>
        """

        html_code = BeautifulSoup(html_code, 'html.parser').prettify()

        # Update the Readings file
        readings_file = os.path.join(subjects_dir, subject, 'README.md')
        with open(readings_file, 'w') as file:
            file.write(f"# {subject} Readings\n\n")
            file.write(html_code)

if __name__ == "__main__":
    main()