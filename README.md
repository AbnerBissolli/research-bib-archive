# Research Bib Archive

The **research-bib-archive** project helps you organize research readings in a structured and automated manner.

## Structure

1. **Research Subjects Directory**: Create subdirectories for each of your research subjects. For each subject directory, you should have a `references.bib` file containing the BibTeX entries of your readings.

   Example BibTeX entry:

   ```bibtex
   @inproceedings{abneretc23,
     author = {A. F. B. Costa and H. Hepp and M. V. G. Silva and L. M. Zatesko},
     language = {portuguese},
     year = 2023,
     title = {The Hidden Subgroup Problem and Non-interactive Perfect Zero-Knowledge Proofs},
     booktitle = {Proc. 43rd Congress of the Brazilian Computer Society (CSBC '23/VIII ETC)},
     address = {João Pessoa, Brazil},
     issn = {2595-6116},
     url = {https://doi.org/10.5753/etc.2023.230017},
     pages = {99--103},
   }
   ```

    It is recommended to add `status` and `comment` fields to keep track of your readings:

    ```bibtex
    @inproceedings{abneretc23,
        author = {A. F. B. Costa and H. Hepp and M. V. G. Silva and L. M. Zatesko},
        language = {portuguese},
        year = 2023,
        title = {The Hidden Subgroup Problem and Non-interactive Perfect Zero-Knowledge Proofs},
        booktitle = {Proc. 43rd Congress of the Brazilian Computer Society (CSBC '23/VIII ETC)},
        address = {João Pessoa, Brazil},
        issn = {2595-6116},
        url = {https://doi.org/10.5753/etc.2023.230017},
        pages = {99--103},
        status = {Concluded},  <!-- Status field -->
        comment = {Very Useful}, <!-- Comment field -->
        }
    ```
2. **Status Field**: Use the status field to categorize your readings. The status will also trigger a color-coded indicator and order the list as follows:

     - `Concluded`: 🔵 Articles you have completed reading
     - `Reading`: 🟢 Articles you are currently reading
     - `Queued`: 🟠 Articles you plan to read soon
     - `Pending`: 🟡 Articles that are neither queued nor skipped yet
     - `Skipped`: ⚫️ Articles you decided to skip for now

3. **Automated Updates**: After committing changes to the BibTeX files, GitHub Actions will automatically update the README for each research subject you have created.

# Notes
 - Ensure you follow the directory structure and BibTeX format to maintain consistency.
 - Use the status field to keep track of your progress and organize your readings effectively.
 - Do not forget to verify if the workflow is running properly and its permissions is set to read and write at Settings -> Actions -> Workflow Permissions.