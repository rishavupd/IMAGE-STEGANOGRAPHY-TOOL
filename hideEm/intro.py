from os import chdir, path
import time




def showBrand():
    with open('txtFiles/brand.txt', 'r') as brand:
        lines = [line.rstrip('\n') for line in brand.readlines()]
        for line in lines:
            print(line)
            time.sleep(1 / 50)
    brand.close()
