from sys import stdin

T = int(stdin.readline())
for i in range(T):
    H, W, N = list(map(int, stdin.readline().split()))
    room_num = N // H
    if N % H > 0:
        room_num += 1

    if len(str(room_num)) < 2:
        room_num = '0' + str(room_num)
    if N % H == 0:
        floor_num = H
    else:
        floor_num = N % H

    print(f'{floor_num}{room_num}')
