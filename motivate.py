import os
import pyautogui
import time
from twilio import twiml
from twilio.rest import TwilioRestClient


date_string = time.strftime("%Y-%m-%d-%H:%M")
image_name= date_string+'.png'
im2 = pyautogui.screenshot(image_name)
os.system('mv *.png images/screenShots')
# os.system('mv re')

os.system('open /Users/jhonatancruz/Desktop/Photo\ Booth.app')
# os.system('sh photoBooth.sh')
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


account_sid = "AC3bd3a69773f1ea33cb499e04597dcebe"
auth_token  = "5fc24bcb11f279efe7e608296bc74093"

client = TwilioRestClient(account_sid, auth_token)

client.messages.create(
    to="+9082677299",
    from_="+9088458499",
    media_url="http://www.audubon.org/sites/default/files/styles/engagement_card/public/sfw_apa_2013_28342_232388_briankushner_blue_jay_kk_high.jpg?itok=ttMfUhUu"
    )
