def nnm():
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return

    for a in arr:
        if a not in lst:
            lst.append(a)
            nnm()
            lst.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []

nnm()