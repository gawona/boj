import sys; input = sys.stdin.readline
N = int(input())
number = []
for n in range(N):
    number.append(int(input()))

for i in sorted(number):
    print(i)