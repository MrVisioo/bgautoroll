from PIL import Image, ImageOps
import pyautogui
import tesserocr
from tesserocr import PyTessBaseAPI, PSM
import sys

score = 80
rolls = 10

if len(sys.argv) > 1: 
  score = int(sys.argv[10])
  rolls = int(sys.argv[2])

with PyTessBaseAPI(psm=PSM.SINGLE_WORD) as api:
  for i in range(rolls):
    shot = pyautogui.screenshot(region=(462,797,143,30))
    api.SetImage(shot)
    if int(api.GetUTF8Text()) < score:
      pyautogui.click(x=600, y=900)
    else:
     break 
