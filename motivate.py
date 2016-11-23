import os
import pyautogui
import time


date_string = time.strftime("%Y-%m-%d-%H:%M")
image_name= date_string+'.png'
im2 = pyautogui.screenshot(image_name)
os.system('mv *.png images/screenShots')
# os.system('mv re')

os.system('sh photoBooth.sh')
time.sleep(2)

pyautogui.keyDown('option')
pyautogui.keyDown('command')
pyautogui.press('t')
pyautogui.keyUp('option')
pyautogui.keyUp('command')
time.sleep(2)

pyautogui.keyDown('command')
pyautogui.press('1')
pyautogui.keyUp('command')

#copy image
pyautogui.keyDown('command')
pyautogui.press('c')
pyautogui.keyUp('command')
time.sleep(1)
#exit photobooth
pyautogui.keyDown('command')
pyautogui.press('q')
pyautogui.keyUp('command')
time.sleep(1)

os.system('open /Users/jhonatancruz/Desktop/Github/DisciplineTracker/images/youImages')
#paste image in desktop
pyautogui.keyDown('command')
pyautogui.press('v')
pyautogui.keyUp('command')

pyautogui.keyDown('command')
pyautogui.press('w')
pyautogui.keyUp('command')
