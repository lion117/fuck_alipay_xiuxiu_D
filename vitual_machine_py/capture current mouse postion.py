# -*- coding: utf-8 -*-
"""
@author: Administrator
Date:  16-2-5
Email:	lion_117@126.com
All Rights Reserved Licensed under the Apache License
"""


from pymouse import PyMouse

def main():
    try:
        from pymouse import PyMouseEvent

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
    try:
        size = m.screen_size()
        print("size: %s" % (str(size)))
        i_pos = m.position()
        print("current mouse postion is :%s " % (str(i_pos)))
        # print(i_pos)
    	# pos = (random.randint(0, size[0]), random.randint(0, size[1]))
    except:
        print("error occur")


    try:
        e.stop()
    except:
        pass


if __name__ == '__main__':
    main()
    pass
