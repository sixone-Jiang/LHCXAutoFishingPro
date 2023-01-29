import win32gui
import win32con
import win32api
hwnd = win32gui.FindWindow("灵魂潮汐 - MuMu模拟器", None)
win32api.SetCursorPos([30,150])

def doClick(cx,cy):#第四种，可后台
    long_position = win32api.MAKELONG(cx, cy)#模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)#模拟鼠标按下
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)#模拟鼠标弹起
doClick(1170, 480)
print(1)