import sys
import win32gui
import win32con
import win32api

def send_wheel_down(hwnd, delta=-120):
    # 获取窗口客户区大小
    left, top, right, bottom = win32gui.GetClientRect(hwnd)
    client_width = right - left
    client_height = bottom - top
    
    # 计算中心点坐标（客户区坐标）
    x = client_width // 2
    y = client_height // 2
    
    # 将客户区坐标转换为屏幕坐标
    point = win32gui.ClientToScreen(hwnd, (x, y))
    
    # 构造 lParam: (y << 16) | x
    lParam = win32api.MAKELONG(point[0], point[1])
    
    # 构造 wParam: (delta << 16) | 按键状态(0)
    wParam = win32api.MAKELONG(0, delta)
    
    # 发送 WM_MOUSEWHEEL 消息
    win32gui.PostMessage(hwnd, win32con.WM_MOUSEWHEEL, wParam, lParam)
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mouse_wheel.py <window_title> [delta]")
        sys.exit(1)
    
    window_title = sys.argv[1]
    delta = int(sys.argv[2]) if len(sys.argv) > 2 else -120
    
    # 查找窗口
    hwnd = win32gui.FindWindow(None, window_title)
    if not hwnd:
        print(f"Window not found: {window_title}")
        sys.exit(1)
    
    # 发送滚轮消息
    success = send_wheel_down(hwnd, delta)
    sys.exit(0 if success else 1)