# допускается также
# использовать две
# целочисленные переменные i, k
a = []
n = 2000
for i in range(0, n):
    a.append(int(input()))
k = 0
for i in range(n):
    if a[i] % 2 == 1:
        k += 1
if k % 2 == 0:
    print(k)
else:
    print(n-k)
