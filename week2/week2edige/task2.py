a = input().strip()
b = input().strip()

m = len(b)
bb = b + b

count = 0
for i in range(len(a) - m + 1):
    sub = a[i:i + m]
    if sub in bb:
        count += 1

print(count)
