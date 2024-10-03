#! Python 3.12.5
#  Using user chosen ADJECTIVE, NOUN, ADVERB and VERB.

import re

# Step 1: Open and read the text file.
with open('madlibs_template.txt', 'r') as file:
    content = file.read()

# Step 2: Define placeholders and corresponding prompts
placeholders = {
    'ADJECTIVE': 'Enter an adjective: ',
    'NOUN': 'Enter a noun: ',
    'ADVERB': 'Enter an adverb: ',
    'VERB': 'Enter a verb: '
}

# Step 3: FUnction to replace placeholders with user inputs
def replace_placeholder(match):
    placeholder = match.group(0)    # This gets the actual word (ADJECTIVE, NOUN, etc.)
    prompt = placeholders[placeholder]    # Get the prompt based on the placeholder
    return input(prompt)   # Ask the user for the input

# Step 4: Use re.sub() to replace all placeholders with user input.
filled_content = re.sub(r'ADJECTIVE|NOUN|ADVERB|VERB', replace_placeholder, content)

# Step 5: Display the modified content
print("nHere is your Mad Libs story:\n")
print(filled_content)

# Optional: Save the modified content to a new file
with open('madlibs_filled.txt', 'w') as file:
    file.write(filled_content)
    print("\nYour Mad Libs story has been saved to 'madlibs_filled.txt'")
