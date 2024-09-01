import time
from os import system
from intro import showBrand


def aboutApp():
    system("clear")
    showBrand()
    print("\n")
    aboutFile = open("./txtFiles/description.txt", "r")
    print(aboutFile.read())
    print("\n")
    userInput = input("Press enter to go to main menu")
    if userInput:
        pass
