import os
import shutil

# ANSI escape code for red text and resetting the color to default
RED_TEXT = "\033[31m"
RESET_COLOR = "\033[0m"


def organize_files(source_dir, target_dir):
    """
    Organizes files in the source directory based on their file extensions and moves them to corresponding folders
    in the target directory.

    Parameters:
        source_dir (str): The path to the directory containing unorganized files.
        target_dir (str): The path to the directory where organized files will be moved.

    Returns:
        None
    """

    # Ensure that the target directory exists or create it if it doesn't
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Dictionary to map file extensions to folder names
    extension_to_folder = {
        ".txt": "TextFiles",
        ".pdf": "PDFs",
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".gif": "Images",
        ".doc": "Documents",
        ".docx": "Documents",
        ".xls": "Spreadsheets",
        ".xlsx": "Spreadsheets",
    }

    # Get a list of all files in the source directory
    files = os.listdir(source_dir)

    for file in files:
        file_path = os.path.join(source_dir, file)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(file_path)
            folder_name = extension_to_folder.get(file_extension.lower(), "Other")

            # Create the folder if it doesn't exist
            folder_path = os.path.join(target_dir, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move the file to the corresponding folder
            destination_path = os.path.join(folder_path, file)
            shutil.move(file_path, destination_path)
            print(f"{RED_TEXT}Moved '{file}' to '{folder_name}' folder.{RESET_COLOR}")


if __name__ == "__main__":
    print(f"{RED_TEXT}----- BEFORE YOU START -----")
    print("""Keep in mind to use this program CAUTIOUSLY. This program can be dangerous and you may LOSE your 
essential data during the process. Make sure to take a backup of the files before proceeding.\n""")

    agreement = input(f"{RESET_COLOR}Are you sure you want to continue? (y/n): ").lower()

    if agreement == 'y':
        try:
            source_directory = input("Enter the Source Directory: ")
            target_directory = input("Enter the Target Directory: ")

            organize_files(source_directory, target_directory)

        except Exception as e:
            print(e)

    else:
        print("Aborted. No files were moved.")
