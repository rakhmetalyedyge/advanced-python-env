N = int(input())

if N > 0:
    total = N * (N + 1) // 2
else:
    total = N * (1 + N) // 2 + 1

print(total)