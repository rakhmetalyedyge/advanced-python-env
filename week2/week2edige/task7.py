items = input().split()
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1
most_popular = max(freq, key=freq.get)
once_items = [item for item, count in freq.items() if count == 1]
sorted_items = sorted(freq.items(), key=lambda x: -x[1])
print("Purchase frequency:")
for item, count in freq.items():
    print(f"{item}: {count}")

print("Most popular item:", most_popular)

print("Purchased once:", " ".join(once_items))

print("Sorted by frequency:")
for item, count in sorted_items:
    print(item, count)
