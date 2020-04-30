import pyautogui

print('中断するにはCtrl-cを押してください')

try:
    while True:
        #マウス座標を取得して表示
        x, y = pyautogui.position()
        position_str = 'x:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
        print(position_str, end = '')
        print('\b' * len(position_str), end = '', flush=True)
except KeyboardInterrupt:
    print('\n終了')
