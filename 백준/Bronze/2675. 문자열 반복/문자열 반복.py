T = int(input())
for t in range(T):
    R, S = map(str, input().split())
    res = ''

    for s in S:
        res += s * int(R)

    print(res)