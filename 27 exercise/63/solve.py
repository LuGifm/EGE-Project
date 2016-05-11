"""
Очередь обеспечивает оптимизацию по скорости алгоритма.
Обязательная чётность произведения требует хранения и чётных и нечётных максимумов.

"""
n = int(input())

a = []
for x in range(9):
    a.append(int(input()))
R = -1
max_2 = -1
max_n = -1
for x in range(n-9):
    y = int(input())
    if a[0] % 2 == 0 and a[0] > max_2:
        max_2 = a[0]
    elif a[0] % 2 == 1 and a[0] > max_n:
        max_n = a[0]
    if max_n*y > R and max_n*y % 2 == 0:
        R = max_n*y
    if max_2*y > R:
        R = max_2*y
    a.pop(0)
    a.append(y)
print(R)
