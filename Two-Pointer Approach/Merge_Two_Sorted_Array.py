a = [1, 2, 3]
b = [4, 5, 6]

m = len(a)
n = len(b)

i = 0
j = 0

res = []

while i < m and j < n:
    if a[i] <= b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1
while j < n:
    res.append(b[j])
    j += 1

while i < m:
    res.append(a[i])
    i += 1

print(res)
