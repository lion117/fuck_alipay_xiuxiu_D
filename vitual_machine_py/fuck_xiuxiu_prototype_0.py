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




def main():
    try:
        class event(PyMouseEvent):
            def move(self, x, y):
                print("Mouse moved to", x, y)

            def click(self, x, y, button, press):
                if press:
                    print("Mouse pressed at", x, y, "with button", button)
                else:
                    print("Mouse released at", x, y, "with button", button)
        e = event()
        #e.capture = True
        e.start()

    except ImportError:
        print("Mouse events are not yet supported on your platform")

    m = PyMouse()
    i_pos = (1179,287)
    i_counts = 0
    m.move(i_pos[0] , i_pos[1])

    while(i_counts < 10):

        time.sleep(0.5)
        m.click(i_pos[0], i_pos[1], 1)
        time.sleep(0.6)
        m.click(i_pos[0], i_pos[1], 1)

        i_counts+= 1

    try:
        e.stop()
    except:
        pass


if __name__ == '__main__':
    main()
    pass
