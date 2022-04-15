import pyautogui
from time import sleep
#屏幕大小
size=pyautogui.size()
#鼠标位置
mouse_pos=pyautogui.position()
sleep(5)
help_pos=pyautogui.locateOnScreen('./屏幕截图 2022-02-04 203904.png')
#获取按键中心点
goto_pos=pyautogui.center(help_pos)
pyautogui.moveTo(goto_pos,duration=1)
#点击
while True:
    pyautogui.click(button='left')