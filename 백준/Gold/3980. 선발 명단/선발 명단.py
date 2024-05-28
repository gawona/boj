from sys import stdin; input = stdin.readline

def select(i):
    global power, max_power
    if i == 11:
        max_power = max(power, max_power)
        return

    for j in range(11):
        if arr[i][j] and not position[j]:
            position[j] = True
            power += arr[i][j]
            select(i + 1)
            position[j] = False
            power -= arr[i][j]

C = int(input())
for _ in range(C):
    arr = [list(map(int, input().split())) for _ in range(11)]
    position = [False] * 11
    max_power = 0
    power = 0
    select(0)
    print(max_power)