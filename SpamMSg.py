import pyautogui
from time import sleep


print("""\033[33m

   _____                         __  __  _____       
  / ____|                       |  \/  |/ ____|      
 | (___  _ __   __ _ _ __ ___   | \  / | (___   __ _ 
  \___ \| '_ \ / _` | '_ ` _ \  | |\/| |\___ \ / _` |
  ____) | |_) | (_| | | | | | | | |  | |____) | (_| |
 |_____/| .__/ \__,_|_| |_| |_| |_|  |_|_____/ \__, |
        | |                                     __/ |
        |_|                                    |___/ 
     by mousavi 
    
\033[39m""")

Msg = input('\033[33m [01] \033[39m Enter Your Msg>> : ')
num_msg = int(input("\033[33m [02] \033[39mChose Your Number Of Msg>> : "))
time_msg = float(input("\033[33m [03] \033[39m Chose Your Time Of Msg>> : "))

for num in range(num_msg):
    pyautogui.typewrite(Msg)
    sleep(time_msg)
    pyautogui.press('enter')
    sleep(time_msg)