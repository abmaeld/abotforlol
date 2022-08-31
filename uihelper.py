import pyautogui
import keyboard
from PIL import Image

def click(path='none', grayscale=False, confidence=.7, button='left', clicks=1, interval=.35, duration=.35):
  try:
    image = pyautogui.locateCenterOnScreen(path, grayscale=grayscale, confidence=confidence);
    if image != None:
      pyautogui.click(image.x, image.y, clicks=clicks, interval=interval, button=button, duration=duration);
      return True;
  except:
    return False;
    pass;
  return False;
