import pyautogui
from tesserocr import PyTessBaseAPI, PSM
import sys

bcord = pyautogui.locateOnScreen('rollb.png')  # locate roll button on screen
if bcord is not None:
    # assuming window size and location is a constant !TBC
    # determine coordinates to look for score depending on location of the
    # button
    ocr_left = bcord.left - 48
    ocr_top = bcord.top - 74
    ocr_width = 143
    ocr_height = 30
    ocr_box = (ocr_left, ocr_top, ocr_width, ocr_height)
    # same but for coordinate to click on too roll
    click_x = bcord.left + 90
    click_y = bcord.top + 29
    # default values
    score = 80
    rolls = 1  # num. of attempts
    # look for command line arguments
    if len(sys.argv) > 1:
        score = int(sys.argv[1])
    if len(sys.argv) > 2:
        rolls = int(sys.argv[2])
    # using tesseract to recognize text
    # and pyautogui to capture information from game screen
    # we click on the button until we get hight enough score
    with PyTessBaseAPI(psm=PSM.SINGLE_WORD) as api:
        for i in range(rolls):
            shot = pyautogui.screenshot(region=ocr_box)
            api.SetImage(shot)
            if int(api.GetUTF8Text()) < score:
                pyautogui.click(x=click_x, y=click_y)
            else:
                break
