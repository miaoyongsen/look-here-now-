from threading import Timer             #自动执行多线程
import time
import pyautogui                        #终端输入库

def a():
    pyautogui.click(1000, 500)          #点击像素点
    pyautogui.typewrite('mkdir a')      #创建a文件
    pyautogui.typewrite(['enter'])      #回车
    pyautogui.typewrite('cd a')         #移动到a目录
    pyautogui.typewrite(['enter'])
    print(time.time())                  #打印当前时间
    t = Timer(10, a)                    #每10s执行一次a函数
    t.start()                           #开始
if __name__ == '__main__':
    a()                                 #调用函数