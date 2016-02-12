# -*- coding: utf-8 -*-
"""
@author: Administrator
Date:  16-2-5
Email:	lion_117@126.com
All Rights Reserved Licensed under the Apache License
"""


from pymouse import  PyMouse
from pymouse import PyMouseEvent
import  time
import pyHook
import pythoncom
import thread
import threading

is_run = False





def mouse_simulate():
    try:
        class event(PyMouseEvent):
            def move(self, x, y):
                pass

            def click(self, x, y, button, press):
                if press:
                    print("Mouse pressed at", x, y, "with button", button)
                else:
                    print("Mouse released at", x, y, "with button", button)
        e = event()
        e.start()

    except ImportError:
        print("Mouse events are not yet supported on your platform")

    m = PyMouse()

    t_corr = (1173,313)
    i_pos = t_corr
    m.move(i_pos[0] , i_pos[1])

    while(True):
        if is_run is False:
            time.sleep(1)
        else:
            time.sleep(0.2)
            m.click(i_pos[0], i_pos[1])

    try:
        e.stop()
    except:
        pass





def onKeyboardEvent(event):
    "处理键盘事件"
    print("WindowName:%s\n" % str(event.WindowName))
    print("Key:%s\n" % str(event.Key))

    global is_run

    if event.Key == '1':
        is_run = True
        print("key  == 1")
    elif event.Key == '2':
        is_run = False
        print("key ===  2")

    return True




if __name__ == "__main__":
    # begin to click
    is_run = True
    i_coor = (1181,306)
    i_handle = threading.Thread(target = mouse_simulate )
    i_handle.start()
    #创建hook句柄
    hm = pyHook.HookManager()
    #监控键盘
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    #循环获取消息
    pythoncom.PumpMessages()



