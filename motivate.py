import os
import pyautogui
import time

os.system('ls')
os.system('sh photoBooth.sh')
time.sleep(3)


pyautogui.keyDown('option')
pyautogui.keyDown('command')
pyautogui.press('t')
pyautogui.keyUp('option')
pyautogui.keyUp('command')
time.sleep(3)

pyautogui.press('left')
time.sleep(1)
#copy image
pyautogui.keyDown('command')
pyautogui.press('c')
pyautogui.keyUp('command')
time.sleep(1)
#exit photobooth
pyautogui.keyDown('command')
pyautogui.press('q')
pyautogui.keyUp('command')

#paste image in desktop
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')
