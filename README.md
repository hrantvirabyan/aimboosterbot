# aimboosterbot
This is a bot that will give you aimbot in the game aimbooster. Since the game is bounded to my screen of 1920x1080, the program uses a for loop between those pixels in order to set the cursor position and click. 

If you are running on the same resolution, make sure to set it to fullscreen in order for it to work. 

If you want to change it to the size of your screen, run a python idle window, import pyautogui, and enter pyautogui.displayMousePosition().

It will start printing the current mouse pos. Drag it to the game screen and set the "pic = pyautogui.screenshot(region=(445,105,1300,910))" pixels according to your needs. The first two arguments are where your game screen starts, so the top left. The 3rd and 4th arguments would be the size of your game. 

Furthermore, you would need to change the "click(x+445, y+105)". The numbers added should be the top left of your game screen. 

You can do this with or without fullscreen if you adjust the size of the screen correctly.

________________________________________________________________________________________________________________________________________________________________________

https://user-images.githubusercontent.com/113553059/195214334-3a72e33a-4adf-4a88-819a-a1cb0a6b46ae.mp4

