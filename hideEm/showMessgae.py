import base64
import hashlib
from cryptography.fernet import Fernet
import time
import os
from datetime import datetime

from intro import showBrand
import selectImage as si
from PIL import Image

escSeqForMessage = "001000000101101101000101010011100100010001011101"
escSeqForPassword = "01011011011110110101111001011101"
passwordFlag = 0
wrongCount = 0
fileExp = ""
passkey = ""
passToDecrypt = ""


def writeTextToFile(text):
    global imgName, fileExp
    fileName = f"{os.path.expanduser('~')}/{datetime.now()}.txt"
    fileExp = fileName
    openFile = open(fileName, 'w')
    openFile.write(text)


def refineText(text):
    global passkey
    refinedText = text.replace(f"{passkey}b'", "")
    refinedText = refinedText.replace("' [END]", "")
    return refinedText


def hold(text):
    checkToExit = input("\nEnter 'q!' to exit without saving and 'w!' to save and exit: ")
    if checkToExit == 'q!':
        return
    elif checkToExit == 'w!':
        writeTextToFile(text)
        si.clear()
        print(f"Your message is saved in {fileExp}")
        holding = input("Enter to continue...")
    else:
        hold(text)


def display(text):
    global passToDecrypt
    fernet = Fernet(passToDecrypt)
    text = fernet.decrypt(bytes(text, 'ascii'))
    text = str(text)
    remove = text[:2]
    text = text.replace(remove, "")
    remove = text[-1]
    text = text.replace(remove, "")
    return text


def checkPassword():
    global escSeqForPassword, imgName, passwordFlag, wrongCount, passkey, passToDecrypt
    password = input("Decryption Key (to goto menu: [MAIN]): ")
    si.clear()

    if password == '[MAIN]':
        returnFlag = '[MAIN]'
        return returnFlag
    else:
        remain = 32 - len(password)
        password = password + "0" * remain
        passByte = bytes(password, 'ascii')
        hashPass = hashlib.md5(passByte)
        basePass = base64.b64encode(passByte)
        password = str(hashPass.digest()) + '[{^]'

        passkey = password
        passToDecrypt = basePass
        encodedPassword = ""

        passwordFromImage = ""
        for char in password:
            acsiiOfChar = ord(char)
            binOfChar = f"{acsiiOfChar:08b}"
            encodedPassword = encodedPassword + binOfChar

        img = Image.open(imgName)
        for y in range(img.size[1]):
            if len(passwordFromImage) >= 32:
                if passwordFromImage[-32:] == escSeqForPassword:
                    break
            for x in range(img.size[0]):
                r, g, b = img.getpixel((x, y))
                binR = f'{r:08b}'
                passwordFromImage = passwordFromImage + binR[6:]
                if len(passwordFromImage) >= 32:
                    if passwordFromImage[-32:] == escSeqForPassword:
                        break

        if passwordFromImage == encodedPassword:
            return '[YES]'
        else:
            return "[NO]"


def show(imageName):
    global escSeqForMessage, passwordFlag, wrongCount, imgName
    imgName = imageName
    passwordFlag = 0
    wrongCount = 0
    si.clear()

    status = checkPassword()
    if status == '[YES]':
        print(f"Selecting image {imageName}\n")
        binText = ""
        img = Image.open(imageName)

        for y in range(img.size[1]):
            if len(binText) >= 48:
                if binText[-48:] == escSeqForMessage:
                    break
            for x in range(img.size[0]):
                r, g, b = img.getpixel((x, y))
                binR = f"{r:08b}"
                binText = binText + binR[6:]
                if len(binText) >= 48:
                    if binText[-48:] == escSeqForMessage:
                        break

        startText = 0
        endText = startText + 8
        decodedMessage = ""

        loopBinText = len(binText) / 8
        loopCount = 0
        while loopCount < loopBinText:
            slicedBits = binText[startText: endText]
            startText = startText + 8
            endText = startText + 8
            desSlicedBits = int(str(slicedBits), 2)
            decodedMessage = decodedMessage + chr(desSlicedBits)
            loopCount = loopCount + 1

        print("Message extracted successfully...")
        time.sleep(1)
        si.clear()
        os.chdir(f"{os.path.dirname(__file__)}")
        showBrand()
        print("\nMessage::")
        refinedText = refineText(decodedMessage)
        decryptedText = display(refinedText)
        print(decryptedText)
        hold(decryptedText)

    elif status == '[NO]':
        input("\nYou entered wrong password...")
    else:
        print("\nUnknown error occurred...")


message = ""
imgName = ""
