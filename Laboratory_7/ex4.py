# Write a Python script that counts the number of files with each extension in a given directory. The script should:
#    Accept a directory path as a command line argument (using sys.argv).
#    Use the os module to list all files in the directory.
#    Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
#    Include error handling for scenarios such as the directory not being found, no read permissions, or the directory being empty.

import os
import sys
from collections import defaultdict

def count_file_extensions(directory):
    extension_counts = defaultdict(int)
    try:
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"The path {directory} is not a valid directory.")

        for root, _, files in os.walk(directory):
            for file in files:
                _, ext = os.path.splitext(file)
                extension_counts[ext] += 1

        if not extension_counts:
            print("The directory is empty or contains no files.")
        else:
            for ext, count in extension_counts.items():
                print(f"{ext}: {count}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        count_file_extensions(directory_path)