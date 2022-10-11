from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#2 seconds to start the script and get into the game
time.sleep(2)

#click function
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (255, 219, 195)

#as long as q is not pressed, the while loop will continue
while keyboard.is_pressed('q') == False:
    temp = 0
    #area for the full game of aimbooster on a 1920x1080 monitor
    pic = pyautogui.screenshot(region=(445,105,1300,910))
    #grabs the height and width of the "screenshot" that was taken
    width, height = pic.size

#for loop that will go through every 5 pixels in order to see if the color of the target matches the pixel
    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = pic.getpixel((x, y))

            if r==255 and g == 219 and b==195:
                temp = 1
                click(x+445, y+105)
                time.sleep(0.05)
                break

        if temp == 1:
            break
