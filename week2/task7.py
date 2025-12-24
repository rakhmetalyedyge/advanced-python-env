items = input().split()

freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

print("Purchase frequency:")
for item, count in freq.items():
    print(f"{item}: {count}")

most_popular = max(freq, key=freq.get)
print("Most popular item:", most_popular)

once = [item for item, count in freq.items() if count == 1]
print("Purchased once:", " ".join(once))

print("Sorted by frequency:")
for item, count in sorted(freq.items(), key=lambda x: -x[1]):
    print(item, count)