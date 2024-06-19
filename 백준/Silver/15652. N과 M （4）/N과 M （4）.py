def nnm(k):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return

    for i in range(k, n+1):
        lst.append(i)
        if not lst:
            nnm(k)
        elif i >= lst[-1]:
            nnm(lst[-1])
        lst.pop()

n, m = map(int, input().split())
lst = []

nnm(1)