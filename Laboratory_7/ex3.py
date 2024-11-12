# Create a Python script that calculates the total size of all files in a directory provided as a command line argument. The script should:
#
# Use the sys module to read the directory path from the command line.
# Utilize the os module to iterate through all the files in the given directory and its subdirectories.
# Sum up the sizes of all files and display the total size in bytes.
# Implement exception handling for cases like the directory not existing, permission errors, or other file access issues.

import os
import sys

def calculate_total_size(directory):
    total_size = 0
    try:
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"The path {directory} is not a valid directory.")

        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    total_size += os.path.getsize(file_path)
                except Exception as e:
                    print(f"Error accessing file {file_path}: {e}")
    except Exception as e:
        print(f"Error: {e}")
    return total_size

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        total_size = calculate_total_size(directory_path)
        print(f"Total size: {total_size} bytes")