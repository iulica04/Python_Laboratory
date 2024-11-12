#Create a Python script that does the following:
#       Takes a directory path and a file extension as command line arguments (use sys.argv).
#       Searches for all files with the given extension in the specified directory (use os module).
#       For each file found, read its contents and print them.
#       Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.


import os
import sys


def read_files_in_directory(directory, extension):
    try:
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"The path {directory} is not a valid directory.")

        if not extension.startswith('.'):
            raise ValueError("The file extension should start with a dot (e.g., .txt).")

        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as f:
                            print(f"Contents of {file_path}:")
                            print(f.read())
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]
        read_files_in_directory(directory_path, file_extension)