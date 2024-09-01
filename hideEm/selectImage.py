import os
import time

def clear():
    os.system('cls')


def showErr():
    global error
    return error


def start():
    global admin, userDir, error
    if len(error) > 0:
        print(f'\nError::: {showErr()}\n')
        error = ""
        time.sleep(0.5)
    userDir = input("Directory you want to begin with (/): ")
    if userDir != "" and os.path.exists(userDir):
        select()
    elif userDir == "":
        print("\nSelecting root (/) directory as default directory\n")
        userDir = "../Users/dell/Desktop/8th sem/final year project/PSNR calc/test_image"
        time.sleep(0.5)
        select()
    elif not os.path.exists(userDir):
        error = "Given directory is not valid"
        time.sleep(0.5)
        start()
    else:
        print(f"\nError on selection: Please report to {admin}\n")


def getLenOfDir():
    global userDir
    return len(os.listdir(userDir))


def select():
    global userDir, error, imageName, admin

    cls()

    if len(error) > 0:
        print(f'\nError::: {showErr()}\n')
        error = ""

    print(f"You are on (0 to main menu): [+]{userDir}")
    for count, file in enumerate(os.listdir(userDir)):        
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or not file.startswith("."):
            print(f"++[{count + 1}]\t{file}")

    try:
        fileNumber = int(input(f"Select file number (1-{getLenOfDir()}): "))
        if getLenOfDir() >= fileNumber >= 1:
            selectedFile = os.listdir(userDir)[fileNumber - 1]
            newUserDir = f"{userDir}/{selectedFile}"
            if os.path.isdir(newUserDir) and '.' not in selectedFile:
                os.chdir(newUserDir)
                userDir = newUserDir
                select()
            else:
                if selectedFile.endswith('.png') or selectedFile.endswith('.jpg') or selectedFile.endswith('.jpeg'):
                    imageName = f'{userDir}/{selectedFile}'
                else:
                    error = "Only .jpeg and .jpg file format are supported for now"
                    select()

        elif fileNumber == 0:
            end()

        else:
            error = "Number out of range"
            select()
    except ValueError:
        error = "Only numbers accepted"
        select()


def getName():
    global imageName
    return imageName


def end():
    global imageName
    imageName = "[EXIT]"


admin = ""
error = ""
imageName = None
userDir = None
