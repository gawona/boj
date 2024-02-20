from sys import stdin; input = stdin.readline
a, b = input().split()

for i in a:
    if i in b:
        a_idx = a.index(i)  # 1
        b_idx = b.index(i)  # 4
        break

lst = [['.'] * len(a) for _ in range(len(b))]
for i in range(len(b)):
    if i == b_idx:
        lst[i] = a
    for j in range(len(a)):
        if lst[i][j] == '.' and j == a_idx:
            lst[i][j] = b[i]

for i in range(len(b)):
    for j in range(len(a)):
        print(lst[i][j], end='')
    print()