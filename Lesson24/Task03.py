alphabet = ['a', 'b', 'c', 'd', 'e']
counts = [10, 34, 23, 17, 56]

for i in range(len(counts) - 1):
    for j in range(len(counts) - 1 - i):
        if counts[j] < counts[j + 1]:
            counts[j], counts[j + 1] = counts[j + 1], counts[j]
            alphabet[j], alphabet[j + 1] = alphabet[j + 1], alphabet[j]

# print(alphabet)
# print(counts)

alphabet = {'a': 10, 'b': 34, 'c': 23, 'd': 17, 'e': 56}

print(alphabet['a'])
