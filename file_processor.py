# File Processor - File: file_processor.py
# Handles reading and merging of text files.
# Version: 1.0
# Created: 2023-12-01
# Author: Kaos

def merge_files(file_paths):
    with open("merged_output.txt", "w") as output_file:
        for path in file_paths:
            with open(path, "r") as file:
                output_file.write(f"{path}\n\n")
                output_file.write(file.read())
                output_file.write("\n\n")

    print("Files merged into 'merged_output.txt'")
