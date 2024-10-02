#! Python 3.12.5
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyboard.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list  - Loads all keywords to clipboard.


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')


# TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

# Delete a specific keyword
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    # Check if the keyword exists before deleting.
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
        print(f"Deleted '{sys.argv[2]}' from the shelf.")
    else:
        print(f"'{sys.argv[2]}' not found in the shelf.")

# List keywords or load content to the clipboard
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print("List of keywords copied to clipboard.")
    # Load content associated with the given keyword.
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sysargv[1]])
        print(f"Copied content for '{sys.argv[1]}' to clipboard.")
    else:
        print(f"'{sys.argv[1]}' not found in the shelf.")
#   elif sys.argv[1] in mcbShelf:
#        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()
