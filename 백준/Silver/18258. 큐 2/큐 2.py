from collections import deque
from sys import stdin; input = stdin.readline
two = deque()
N = int(input())
for n in range(N):
    q_lst = list(input().split())

    if q_lst[0] == 'push':
        two.append(int(q_lst[1]))

    elif q_lst[0] == 'front':
        if not two:
            print(-1)
        else:
            print(two[0])

    elif q_lst[0] == 'back':
        if not two:
            print(-1)
        else:
            print(two[-1])

    elif q_lst[0] == 'size':
        print(len(two))

    elif q_lst[0] == 'empty':
        if not two:
            print(1)
        else:
            print(0)

    elif q_lst[0] == 'pop':
        if not two:
            print(-1)
        else:
            print(two.popleft())