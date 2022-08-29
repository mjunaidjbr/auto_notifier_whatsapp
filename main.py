import os
import random
import pyautogui
import sys
from time import sleep


WAIT = 4
sleep(5)
SCREEN_X, SCREEN_Y = pyautogui.size()
IMG_PATH = os.path.join(os.getcwd(), "img\Main_title_bar")
IMG_PATH_SUB_MAIN = os.path.join(os.getcwd(), "img\sub_main_title_bar")
IMG_FILES = [
    os.path.join(IMG_PATH, f)
    for f in os.listdir(IMG_PATH)
    if os.path.isfile(os.path.join(IMG_PATH, f))
]
IMG_FILES_SUB_MAIN = [
    os.path.join(IMG_PATH_SUB_MAIN, f)
    for f in os.listdir(IMG_PATH_SUB_MAIN)
    if os.path.isfile(os.path.join(IMG_PATH_SUB_MAIN, f))
]
IMG_FILES.sort()
IMG_FILES_SUB_MAIN.sort()
# print(IMG_FILES)
# print(IMG_FILES_SUB_MAIN)

def move_mouse():

    x = random.randint(0, SCREEN_X)
    y = random.randint(0, SCREEN_Y)
    pyautogui.moveTo(x, y, random.uniform(0.3, 1.5))
    sleep(WAIT / 2)


def click_btn(btn):

    x, y = btn
    pyautogui.moveTo(x, y, 0.7, pyautogui.easeInQuad)
    pyautogui.click()


def get_btn(btn_img):
    return pyautogui.locateCenterOnScreen(btn_img, confidence=0.7)


def routine():
    for img_file in IMG_FILES:

        btn = get_btn(img_file)
        if btn != None:
            if img_file.endswith('1_My_Business.png'):
                for _ in range(10):
                    move_mouse()
                click_btn(btn)
                b = random.randint(0, len(IMG_FILES_SUB_MAIN) - 1)
                sleep(WAIT)
                click_btn(get_btn(IMG_FILES_SUB_MAIN[b]))
                sleep(WAIT) 
            else:
                for _ in range(10):
                    move_mouse()
                click_btn(btn)
                sleep(WAIT)


def main():
    while True:
        try:
            routine()

        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
