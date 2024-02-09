from sys import stdin

N = int(stdin.readline())
numbers = list(stdin.readline())

num_sum = 0
for i in range(N):
    if numbers[i] == '\n':
        break
    else:
        num_sum += int(numbers[i])

print(num_sum)