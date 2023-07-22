# File Organizer Tool

File Organizer Tool is a Python script designed to automate file organization based on file extensions. The tool scans a specified source directory, categorizes files into corresponding folders, and then moves them to a target directory. This helps keep files well-organized and simplifies file management tasks.

## Requirements

- Python 3.x

## How to Use

1. Clone the repository or download the `file_organizer.py` script to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the `file_organizer.py` script is located.

3. Run the script using Python by providing the source and target directories as inputs.

   ```
   python file_organizer.py
   ```

4. Follow the instructions displayed on the terminal:
   - Enter the path to the source directory containing unorganized files.
   - Enter the path to the target directory where the organized files will be moved.

5. The script will organize the files based on their file extensions into corresponding folders such as 'TextFiles', 'PDFs', 'Images', 'Documents', 'Spreadsheets', etc. Files with unknown extensions will be moved to an 'Other' folder.

**Note:** Use this tool with caution, as it involves moving files, and data loss may occur if not used carefully. Always take a backup of your important files before proceeding.

## Supported File Types

The File Organizer Tool currently supports the following file extensions:

- `.txt`: Text Files
- `.pdf`: PDF Files
- `.jpg`: JPEG Images
- `.jpeg`: JPEG Images
- `.png`: PNG Images
- `.gif`: GIF Images
- `.doc`: Microsoft Word Documents
- `.docx`: Microsoft Word Documents
- `.xls`: Microsoft Excel Spreadsheets
- `.xlsx`: Microsoft Excel Spreadsheets

## Important Information

- The script uses ANSI escape codes to display some messages in red in the terminal to draw attention to important warnings. The appearance of colored text may vary depending on the terminal or console used.

- The script assumes you have appropriate permissions to access the source and target directories.

- Be cautious when using this tool, especially when providing directory paths, as incorrect paths may result in unintended behavior.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code according to the terms of the license.
