#! Python 3.12.5
# regexSearch.py - A program that opens all .txt files in a folder and prints all existing regexes.

import os  # We need this to work woth folders and files.
import re    # We need this to search for patterns (words) in thetext.

# Step 1: Ask the user for the folder path where the .txt files are.
# This is like asking: "Where should I look for the text files?"
folder_path = input("Enter the path to the folder where yor .txt files are: ")

# Step 2: Ask for  the regular expression (pattern) the user wants to search for.
#This is like asking: "What are you looking for in the files?"
pattern = input("Enter the regular expression to search for: ")

#Step 3: Compile the regular expression to make searching faster.
# Get the pattern ready to search (this makes searching faster).
regex = re.compile(pattern)

# Step 4: Check if the folder exists.
# If the folder is not there, we ell the user and stop.
if not os.path.exists(folder_path):
    print(f"The folder '{folder_path}' doesnot exist.")
else:
    # Step 5: Go through each file in the folder.
    for filename in os.listdir(folder_path):
        # Step 6: Only look at files that end with '.txt'.
        # This means we're only looking at text files, not other types of files.
        if filename.endswith('.txt'):
            # Combine the folder path and filename to get the full path.
            file_path = os.path.join(folder_path, filename)
            print(f"\nSearching in file: {filename}")
            found_match = False    # Initialize 'found_match' for each file
            try:
                # Step 7: Open the file and read its content line by line.
                with open(file_path, 'r') as file:
                    # Step 8: Chec each line to see if it matches the pattern (regex).
                    for i, line in enumerate(file, 1): # Line number starts from 1. We count lines starting from 1.
                        line = line.strip()   # Remove leading/trailing spaces. Remove extra spaces around the text.
                        if regex.search(line):    # Does the line have the word we're looking for?
                            # Step 9: Print the matching lines along with their line number.
                            print(f"Line {i}: {line}")
                            found_match = True   # Set this to True if a match is found
                if not found_match:    # If no match is found, tell the user
                    print("No matches found.")
            except Exception as e:
                # If there's a problem opening the file, we say there's an error.
                print(f"Error reading file {filename}: {e}")
