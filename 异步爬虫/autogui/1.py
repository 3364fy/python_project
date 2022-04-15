import pyautogui
from time import sleep
#屏幕大小
size=pyautogui.size()
#鼠标位置
mouse_pos=pyautogui.position()
#判断点是否在屏幕上
print(pyautogui.onScreen(100,100))
#移动鼠标
pyautogui.moveTo(10,10,duration=1)
pyautogui.moveTo(size.width/2,size.height/2,duration=1)
#鼠标相对移动
pyautogui.moveRel(100,0,duration=1)

#上一次鼠标位置
last_pos=pyautogui.position()
try:
    while True:
        # 新位置
        new_pos=pyautogui.position()
        if last_pos!=new_pos:
            print(new_pos)
            last_pos=new_pos
except KeyboardInterrupt:
    print('\nExit.')

#获取按键
sleep(2)
help_pos=pyautogui.locateOnScreen()
#获取按键中心点
goto_pos=pyautogui.center(help_pos)
pyautogui.moveTo(goto_pos,duration=1)
#点击
pyautogui.click()

sleep(1)
pyautogui.click(button='left')
pyautogui.typewrite('I like python')
pyautogui.typewrite('\nI like python',0.25)
pyautogui.typewrite(['Enter','g','o','o','d','left','left','left','backspace','G','end','.'],0.25)

#模拟按键
#全选+复制
pyautogui.keyDown('ctrl')
pyautogui.press('a')
pyautogui.press('c')
pyautogui.keyUp('ctrl')
