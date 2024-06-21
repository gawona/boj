#    상0 좌1 하2 우3
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

T = int(input())
for t in range(T):

    arr = list(input())

    # 바라보고 있는 방향
    dir = 0
    # 현재 좌표
    cur = [0, 0]
    # 지나간 좌표들 중 절대값 최솟값/최댓값 좌표
    go_min = [0, 0]
    go_max = [0, 0]

    for a in arr:
        if a == 'F':
            cur[0] += di[dir]
            cur[1] += dj[dir]

            # 최솟값
            if cur[0] < go_min[0]:
                go_min[0] = cur[0]
            if cur[1] < go_min[1]:
                go_min[1] = cur[1]
            # 최댓값
            if cur[0] > go_max[0]:
                go_max[0] = cur[0]
            if cur[1] > go_max[1]:
                go_max[1] = cur[1]

        elif a == 'B':
            cur[0] += di[(dir+2)%4]
            cur[1] += dj[(dir+2)%4]

            # 최솟값
            if cur[0] < go_min[0]:
                go_min[0] = cur[0]
            if cur[1] < go_min[1]:
                go_min[1] = cur[1]
            # 최댓값
            if cur[0] > go_max[0]:
                go_max[0] = cur[0]
            if cur[1] > go_max[1]:
                go_max[1] = cur[1]

        elif a =='L':
            # dir < 4
            dir = (dir + 1) % 4

        elif a == 'R':
            # dir > -1
            dir = (dir - 1) % 4

    print((go_max[0]-go_min[0]) * (go_max[1]-go_min[1]))