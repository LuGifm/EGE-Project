"""
Задачка не имеет отношение к егэ.
В питоне есть встроенные функции решающие задачу оптимально (bin(), list.reverse())
Различия между программами на разных языках будут огромны.
Задча проверяет знание основных конструкций низкоуровнего языка (С++, Си). std::cin.get() к примеру
Кроме того, полезно знать что такое конечный автомат.

"""
n = int(input())
n = list(bin(n)[2:])
n.reverse()
n.pop()
n = list(map(int,n))
s = 0
is_end = True
count = 0
for x in range(len(n)):
    if is_end == True:
        if n[x] == 0:
            print('E', end='')
            count += 1
        elif n[x] == 1:
            is_end = False
    else:
        if n[x] == 1:
            is_end = True
            print('A', end='')
            count += 1
        elif n[x] == 0:
            is_end = True
            print('P', end='')
print('')
print(count)
