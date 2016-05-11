"""
Произведение не будет делиться на 26, если в его множителях одновременно не будет 2 и 13.
Все множество чисел входных данных разбивается на подможеств.
1) Делящиеся на 26.
2) Делящиеся только на 13.
3) Делящиеся только на 2.
4) Не делящиеся не на 2, ни на 13.


"""

n = int(input())
division_on_2 = (0, 0) # Максимальные числа которые делятся на 2. Первое число всегда больше или равно 2.
division_on_13 = (0, 0)
division_on_never = (0, 0)
for d in range(n):
    x = int(input())
    if x % 26 == 0:
        continue
    elif x % 2 != 0: # Для делящихся на 2.
        if division_on_2[0] <= x:
            division_on_2 = (x, division_on_2[0])
        elif division_on_2[1] < x:
            division_on_2 = (division_on_2[0], x)
    elif x % 13 != 0: # Для делящихся на 13.
        if division_on_13[0] <= x:
            division_on_13 = (x, division_on_13[0])
        elif division_on_13[1] < x:
            division_on_13 = (division_on_13[0], x)
    elif x % 26 != 0: # Для не делящихся не на 2, ни на 3.
        if division_on_never[0] <= x:
            division_on_never = (x, division_on_never[0])
        elif division_on_never[1] < x:
            division_on_never = (division_on_never[0], x)
R = int(input())
R_new = 0 # Дальше проверяем возможные варинанты деления.
R_new = max(division_on_never[0] * division_on_never[1], R_new)
R_new = max(R_new, division_on_never[0] * division_on_2[0])
R_new = max(R_new, division_on_2[0] * division_on_2[1])
R_new = max(R_new, division_on_13[0] * division_on_never[0])
R_new = max(R_new, division_on_13[0] * division_on_13[1])
print('Вычисленное контрольное значение:', R_new, sep=' ')
if R_new <= 0:
    print("Контроль не пройден.")
elif R_new != R:
    print("Контроль не пройден.")
else:
    print('Контроль пройден.')
