eq = input().strip()

a, op, b, _, c = eq

def val(x):
    return int(x)

if a == 'x':
    if op == '+':
        print(val(c) - val(b))
    else:
        print(val(c) + val(b))
elif b == 'x':
    if op == '+':
        print(val(c) - val(a))
    else:
        print(val(a) - val(c))
else:
    if op == '+':
        print(val(a) + val(b))
    else:
        print(val(a) - val(b))