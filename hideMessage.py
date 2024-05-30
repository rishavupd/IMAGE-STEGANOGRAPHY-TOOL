import time
from datetime import datetime
import os
from PIL import Image
from cryptography.fernet import Fernet
import base64
import hashlib


def getText():
    password = input("Password to lock message (Don't use [MAIN] as your password): ")
    os.system("cls")
    remain = 32 - len(password)
    password = password + '0' * remain
    passByte = bytes(password, 'ascii')
    hashPass = hashlib.md5(passByte)
    basePass = base64.b64encode(passByte)
    hashPass = str(hashPass.digest())
    password = hashPass + "[{^]"

    message = input("Enter the message: \n")
    fernet = Fernet(basePass)
    message = bytes(message, 'ascii')
    message = fernet.encrypt(message)
    message = str(message) + " [END]"

    encodedText = ""
    text = password + message
    for char in text:
        acsiiOfChar = ord(char)
        binOfChar = f"{acsiiOfChar:08b}"
        encodedText = encodedText + binOfChar

    return encodedText


def hide(imageName):
    os.system("cls")
    text = getText()
    os.system("cls")
    pixelToHide = len(text) / 2
    img = Image.open(imageName)
    loadImg = img.load()
    pixelCount = 0
    textStart = 0
    textEnd = textStart + 2
    for y in range(img.size[1]):
        if pixelCount == pixelToHide:
            break
        for x in range(img.size[0]):
            r, g, b = img.getpixel((x, y))
            binR = f"{r:08b}"
            textSection = text[textStart: textEnd]
            textStart = textStart + 2
            textEnd = textStart + 2
            encodedBinR = binR[:6] + textSection
            encodedDecR = int(encodedBinR, 2)
            loadImg[x, y] = (encodedDecR, g, b)
            pixelCount = pixelCount + 1

            if pixelCount == pixelToHide:
                break

    img.save(f"{os.path.expanduser('~')}/encoded-{datetime.now()}.{'jpg'}", format="jpg")
    img.close()
    print("\nMessage hidden successfully...")
    time.sleep(1)


