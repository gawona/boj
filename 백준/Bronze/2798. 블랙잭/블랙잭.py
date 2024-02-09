from sys import stdin

N, M = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))

max_sum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            card_sum = cards[i] + cards[j] + cards[k]
            if card_sum <= M:
                max_sum = max(max_sum, card_sum)
print(max_sum)