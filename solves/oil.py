n = int(input())
min_1 = ('', '', 1000000, -1)
min_2 = ('', '', 1000000, -1)
for x in range(n):
    company, street, mark, prise = input().split()
    prise = int(prise)
    mark = int(mark)
    if mark == 92:
        if prise <= min_1[2]:
            if prise < min_1[2]:
                min_2 = min_1
                min_1 = (company, street, prise, 1)
            elif prise == min_1[2]:
                min_1 = (min_1[0], min_1[1], min_1[2], min_1[3]+1)
        elif prise <= min_2[2]:
            if prise < min_2[2]:
                min_2 = (company, street, prise, 1)
            elif prise == min_2[2]:
                min_2 = (min_2[0], min_2[1], min_2[2], min_2[3]+1)
if min_2[3] == -1:
    if min_1[3] == 1:
        print(min_1[0], min_1[1], sep=' ')
    elif min_1[3] > 1:
        print(min_1[3])
else:
    if min_2[3] == 1:
        print(min_2[0], min_2[1], sep=' ')
    elif min_2[3] > 1:
        print(min_2[3])
