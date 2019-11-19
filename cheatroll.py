from PIL import Image, ImageOps
import pyautogui
import tesserocr
from tesserocr import PyTessBaseAPI, PSM
import sys

bcord = pyautogui.locateOnScreen('rollb.png')
if bcord is not None:
  ocr_left = bcord.left - 48
  ocr_top = bcord.top - 74
  ocr_width = 143
  ocr_height = 30
  ocr_box = (ocr_left,ocr_top,ocr_width,ocr_height)

  click_x = bcord.left + 90
  click_y = bcord.top + 29

  score = 80
  rolls = 1

  if len(sys.argv) > 1: 
    score = int(sys.argv[1])
  if len(sys.argv) > 2:
    rolls = int(sys.argv[2])

  with PyTessBaseAPI(psm=PSM.SINGLE_WORD) as api:
    for i in range(rolls):
      shot = pyautogui.screenshot(region=ocr_box)
      api.SetImage(shot)
      if int(api.GetUTF8Text()) < score:
        pyautogui.click(x=click_x, y=click_y)
      else:
        break
