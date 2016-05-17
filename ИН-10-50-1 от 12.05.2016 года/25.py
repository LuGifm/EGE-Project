# Допускается использовать целочисленные переменные m, k.
a = []
N = 2016
for i in range(0, N):
    a.append(int(input()))
m = 1
for k in range(N):
    if a[k] % 2 == 0:
        if m % 2 == 1 or a[k] > m:
            m = a[k]
    else:
        if m % 2 == 1 and a[k] > m:
            m = a[k]
print(m)
