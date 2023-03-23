a = ["a", "b", "c", "d", "e", "f"]
b = []
for i in range(1, len(a), 2):
    if i % 2 == 1:
        b.append(a[i])

print(b)