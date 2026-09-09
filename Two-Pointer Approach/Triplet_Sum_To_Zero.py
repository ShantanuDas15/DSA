a = [-1, 0, 1, 2, -1, -4]

triplet = []

a.sort()

for i in range(len(a) - 2):
    if i > 0 and a[i] == a[i - 1]:
        continue

    low = i + 1
    high = len(a) - 1

    while low < high:
        total = a[i] + a[low] + a[high]

        if total == 0:
            triplet.append([a[i], a[low], a[high]])
            left = a[low]
            right = a[high]

            while low < high and left == a[low]:
                low += 1

            while low < high and a[high] == right:
                high -= 1

        elif total > 0:
            high -= 1

        else:
            low += 1

print(triplet)
