import os

import selectImage as si
import time
import intro
import about
import hideMessage as hm
import showMessgae as sm


def checkPython():  
    check = os.system('python --version')
    check2 = os.system('python3 --version')
    if check != 0 and check2 != 0:
        print("Err:: This program needs python to run. Please install python and try again...")
        quit()


def showErr():
    global error
    return error
    error = ""


def main(ack):
    os.chdir(f"{os.path.dirname(__file__)}")
    global error
    si.clear()
    intro.showBrand()

    if ack == "hidden":
        print(f"\nYour message is hidden in {os.path.expanduser('~')}")
    if ack == "about":
        print(f"\nDeveloped by Suvam and team! ")

    if len(error) > 1:
        print(f'\nError::: {showErr()}\n')

    print("\nMain menu of hideEm\n")
    print("++[0]\tExit\n")
    print("++[1]\tHide message in image")
    print("++[2]\tRead message from image")
    print("++[3]\tAbout the application")
    print("\n")

    try:
        selectedNumber = int(input(f"Select your option (0-{optionRange}): "))
        if selectedNumber == 0:
            si.clear()
            print(open("./txtFiles/smile.txt", "r").read())
            time.sleep(5)
            si.clear()
            quit()
        elif selectedNumber == 1:
            si.start()
            print(f"Full path of your image is {si.getName()}")
            time.sleep(0.5)
            if si.getName() == "[EXIT]":
                main("")
            else:
                hm.hide(si.getName())
                main("hidden")
        elif selectedNumber == 2:
            si.start()
            print(f"Full path of your image is {si.getName()}")
            time.sleep(0.5)
            if si.getName() == "[EXIT]":
                main("")
            else:
                sm.show(si.getName())
                main("shown")
        elif selectedNumber == 3:
            about.aboutApp()
            main("about")
        elif selectedNumber > 3 or selectedNumber < 0:
            error = "Number out of range"
            main("")
        else:
            error = "Unexpected error occurred..."
    except ValueError:
        error = "Only number accepted"
        main("")


os.chdir(f"{os.path.dirname(__file__)}")
error = ""
aspShowRun = False
optionRange = "3"
si.clear()
time.sleep(0.05)
si.clear()
checkPython()
main("")
