a = [0, 1, 2, 4, 4]
target = 4

low = 0
window_sum = 0
res = float("inf")

for high in range(len(a)):
    window_sum += a[high]

    while window_sum >= target:
        res = min(res, high - low + 1)
        window_sum -= a[low]
        low += 1

print(res if res != float("inf") else 0)
