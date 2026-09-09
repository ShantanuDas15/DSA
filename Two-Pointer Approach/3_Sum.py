a = [1, 1, 1, 2, 2, 3, 3, 3]
target = 4

combo = []

low = 0
high = len(a) - 1

while low < high:
    if a[low] + a[high] == target:
        combo.append([a[low], a[high]])
        left = a[low]
        right = a[high]

        while low < high and a[low] == left:
            low += 1

        while low < high and a[high] == right:
            high -= 1

    elif a[low] + a[high] > target:
        high -= 1

    else:
        low += 1

print(combo)
