a = [1, 1, 2, 2, 3]

unique = 1
i = 0

for j in range(1, len(a)):
    if a[i] != a[j]:
        i += 1
        a[i] = a[j]
        unique += 1

print(a[:unique])
