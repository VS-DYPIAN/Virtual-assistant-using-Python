import pyautogui   
#import pyautogui 
from time import sleep   

pyautogui.hotkey('win', 'r') #windows_key + Run</p><p>
pyautogui.typewrite("cmd\n") #cmd to open command prompt
sleep(0.500)       #500 milisecond delay (depends on your computer speed)</p><p><br>#write the code then press enter('\n') thus pc will auto-lock</p><p>
pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n")