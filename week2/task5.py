import re

allowed = set("ABCEHKMOPTXY")
pattern = re.compile(r'^[A-Z]\d{3}[A-Z]{2}$')

n = int(input())
for _ in range(n):
    plate = input().strip()
    if (
        pattern.match(plate)
        and plate[0] in allowed
        and plate[4] in allowed
        and plate[5] in allowed
    ):
        print("Yes")
    else:
        print("No")