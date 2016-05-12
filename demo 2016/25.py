k = 0
for j in range(n-1):
    if 10 <= a[j] <= 99 and 10 <= a[j+1] <= 99:
        k += 1
print(k)
