from sys import stdin

cnt = []
num_max = 0
for i in range(9):
    num = int(stdin.readline())
    num_max = max(num_max, num)
    if num_max == num:
        cnt.append(i+1)
print(num_max)
print(max(cnt))