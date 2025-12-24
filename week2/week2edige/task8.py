s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print("NO")
else:
    count = [0] * 26

    for c in s1:
        count[ord(c) - ord('A')] += 1
    for c in s2:
        count[ord(c) - ord('A')] -= 1

    if all(x == 0 for x in count):
        print("YES")
    else:
        print("NO")
    