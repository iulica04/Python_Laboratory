# Write a script using the os module that renames all files in a specified directory to
# have a sequential number prefix. For example, file1.txt, file2.txt, etc.
# Include error handling for cases like the directory not existing or files that
# can't be renamed.

import os
import sys

def rename_files_in_directory(directory):
    try:
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"The path {directory} is not a valid directory.")

        files = os.listdir(directory)
        files.sort()  # Sort files to ensure consistent ordering

        for index, file in enumerate(files):
            old_path = os.path.join(directory, file)
            if os.path.isfile(old_path):
                new_name = f"file{index + 1}{os.path.splitext(file)[1]}"
                new_path = os.path.join(directory, new_name)
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed {old_path} to {new_path}")
                except Exception as e:
                    print(f"Error renaming file {old_path}: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        rename_files_in_directory(directory_path)