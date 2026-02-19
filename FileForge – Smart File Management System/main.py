"""
FileForge – Smart File Management System
-----------------------------------------
A Python-based file management system that allows users to
create, read, update, rename, append, and delete files.

Features:
- File and folder listing
- File creation
- File reading
- File updating (rename, overwrite, append)
- File deletion
- Structured error handling
"""

from pathlib import Path
import os


# ======================================================
# Utility Function: Display All Files & Folders
# ======================================================

def list_files_and_folders():
    """
    Recursively lists all files and folders
    in the current working directory.
    """
    base_path = Path.cwd()
    items = list(base_path.rglob("*"))

    if not items:
        print("No files or folders found.")
        return

    print("\nAvailable Files & Folders:\n")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")


# ======================================================
# Create File
# ======================================================

def create_file():
    try:
        list_files_and_folders()
        name = input("\nEnter new file name (with extension): ").strip()

        file_path = Path(name)

        if file_path.exists():
            print("File already exists.")
            return

        content = input("Enter content to write in file: ")

        file_path.write_text(content)
        print("File created successfully.")

    except Exception as err:
        print(f"Error occurred: {err}")


# ======================================================
# Read File
# ======================================================

def read_file():
    try:
        list_files_and_folders()
        name = input("\nEnter file name to read: ").strip()

        file_path = Path(name)

        if not file_path.exists() or not file_path.is_file():
            print("File does not exist.")
            return

        content = file_path.read_text()
        print("\n--- File Content ---")
        print(content)

    except Exception as err:
        print(f"Error occurred: {err}")


# ======================================================
# Update File
# ======================================================

def update_file():
    try:
        list_files_and_folders()
        name = input("\nEnter file name to update: ").strip()
        file_path = Path(name)

        if not file_path.exists() or not file_path.is_file():
            print("File does not exist.")
            return

        print("\n1. Rename File")
        print("2. Overwrite File")
        print("3. Append to File")

        choice = input("Select option: ").strip()

        if choice == "1":
            new_name = input("Enter new file name: ").strip()
            file_path.rename(new_name)
            print("File renamed successfully.")

        elif choice == "2":
            new_content = input("Enter new content: ")
            file_path.write_text(new_content)
            print("File overwritten successfully.")

        elif choice == "3":
            append_content = input("Enter content to append: ")
            with file_path.open("a") as f:
                f.write("\n" + append_content)
            print("Content appended successfully.")

        else:
            print("Invalid option selected.")

    except Exception as err:
        print(f"Error occurred: {err}")


# ======================================================
# Delete File
# ======================================================

def delete_file():
    try:
        list_files_and_folders()
        name = input("\nEnter file name to delete: ").strip()
        file_path = Path(name)

        if not file_path.exists() or not file_path.is_file():
            print("File does not exist.")
            return

        confirm = input("Are you sure? (y/n): ").lower()

        if confirm == "y":
            file_path.unlink()
            print("File deleted successfully.")
        else:
            print("Deletion cancelled.")

    except Exception as err:
        print(f"Error occurred: {err}")


# ======================================================
# Main Menu Loop
# ======================================================

def main():
    while True:
        print("\n==== FileForge Menu ====")
        print("1. Create File")
        print("2. Read File")
        print("3. Update File")
        print("4. Delete File")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            create_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            update_file()
        elif choice == "4":
            delete_file()
        elif choice == "5":
            print("Exiting FileForge.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
