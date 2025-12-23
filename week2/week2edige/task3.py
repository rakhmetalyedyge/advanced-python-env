s = input().strip()

op = s[1]

if s[0] == 'x':
    b = int(s[2])
    c = int(s[4])
    if op == '+':
        x = c - b
    else:
        x = c + b

elif s[2] == 'x':
    a = int(s[0])
    c = int(s[4])
    if op == '+':
        x = c - a
    else:
        x = a - c

else:
    a = int(s[0])
    b = int(s[2])
    if op == '+':
        x = a + b
    else:
        x = a - b

print(x)
