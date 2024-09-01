import os
from os import chdir, remove, path, listdir

warning = "This script adds an alias for the main.py file of the aspHide. Only run this file once you move and place " \
          "the program on your ideal location. Only run the file once and can remove setup.py after the operation"

print(warning)

holding = input("\nEnter to continue...")

dirOfHome = path.expanduser("~")
dirOfIndex = f"{path.dirname(__file__)}/main.py"
print(dirOfHome)
dirInHome = listdir(dirOfHome)
for files in dirInHome:
    if files == ".bashrc" or files == ".zshrc":
        openFile = open(f'{dirOfHome}/{files}', 'a')
        addAlias = f"\nalias hideEm='python3 {dirOfIndex}'"
        openFile.write(addAlias)

print("Please reopen the terminal to use alias...")
# chdir(path.dirname(__file__))
# os.remove("setup.py")
