import time

#プログラムの説明を表示
print('enterで開始。再enterで経過時間。Ctrl-Cで終了')

input()
print('start')
start_time = time.time()
last_time = start_time
lap_num = 1

#ラップタイムを計測
try:
    while True:
        input()
        now = time.time()
        lap_time = round(now - last_time, 2)
        total_time = round(now - start_time, 2)
        print('ラップ #{}: {} ({})'.format(lap_num, total_time, lap_time), end='')
        lap_num += 1
        last_time = now
except KeyboardInterrupt:
    #Ctrl-c例外を処理
    print('/n終了')

