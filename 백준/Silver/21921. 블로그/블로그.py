N, X = map(int, input().split())
visitors = list(map(int, input().split()))
sum_visitors = sum(visitors[:X])
visits = [sum_visitors]
for i in range(N - X):
    sum_visitors = sum_visitors - visitors[i] + visitors[i + X]
    visits.append(sum_visitors)
max_visitors = max(visits)

if max_visitors == 0:
    print('SAD')
else:
    print(max_visitors)
    print(visits.count(max_visitors))