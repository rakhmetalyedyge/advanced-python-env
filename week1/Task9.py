ticket = input().zfill(6)
first_half = ticket[:3]
second_half = ticket[3:]
sum_first = sum(int(digit) for digit in first_half)
sum_second = sum(int(digit) for digit in second_half)
if sum_first == sum_second:
    print("YES")
else:
    print("NO")
