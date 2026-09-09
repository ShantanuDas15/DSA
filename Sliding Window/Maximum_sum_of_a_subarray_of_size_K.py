a = [1, 2, 3, 4]
k = 2

window_sum = sum(a[:k])
max_sum = window_sum

for i in range(k, len(a)):
    window_sum += a[i] - a[i - k]
    max_sum = max(max_sum, window_sum)

print(max_sum)
