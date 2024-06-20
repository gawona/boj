def nnm():
    if len(lst) == m:
        temp = []
        for l in lst:
            temp.append(l)
        ans.append(tuple(temp))
        return

    for i in range(n):
        if not visited[i]:
            lst.append(arr[i])
            visited[i] = True
            nnm()
            lst.pop()
            visited[i] = False

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False] * n
lst = []
ans = []

nnm()

ans = list(set(ans))
ans.sort()
for answer in ans:
    print(*answer)