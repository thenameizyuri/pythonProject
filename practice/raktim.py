import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def collide(data):
    for i in range(250,300):
        for j in range(410,563):
            if data[i,j]<100:
                hit('down')
                return

    for i in range(275,415):
        for j in range(563,650):
            if data[i,j]<100:
                hit('up')
                return

    return

if __name__ == "__main__":
    print("Dino game is about to start ")
    time.sleep(3)

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        collide(data)


