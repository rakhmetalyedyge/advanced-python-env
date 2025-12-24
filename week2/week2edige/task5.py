n = int(input())

allowed_letters = set("ABCEHKMOPTXY")

for _ in range(n):
    s = input().strip()

    if len(s) != 6:
        print("No")
        continue

    if (
        s[0] in allowed_letters and
        s[1].isdigit() and
        s[2].isdigit() and
        s[3].isdigit() and
        s[4] in allowed_letters and
        s[5] in allowed_letters
    ):
        print("Yes")
    else:
        print("No")
