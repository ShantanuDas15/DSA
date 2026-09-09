a = [1, 8, 6, 2, 5, 4, 8, 3, 7]

max_area = 0

low = 0
high = len(a) - 1

while low < high:
    h = min(a[low], a[high])
    w = high - low
    area = h * w

    max_area = max(max_area, area)

    if a[low] < a[high]:
        low += 1
    else:
        high -= 1

print(max_area)
