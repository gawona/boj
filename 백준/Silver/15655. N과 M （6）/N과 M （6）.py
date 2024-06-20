def nnm(k):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return

    for i in range(k, len(arr)):
        if arr[i] not in lst:
            lst.append(arr[i])
            nnm(i + 1)
            lst.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lst = []

nnm(0)