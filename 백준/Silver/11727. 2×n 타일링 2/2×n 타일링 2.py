from sys import stdin
n = int(stdin.readline())
tile = [0] * 1001

tile[1] = 1
tile[2] = 3
for i in range(3, n+1):     # 점화식 사용
    tile[i] = tile[i-1] + tile[i-2] * 2

print(tile[n] % 10007)