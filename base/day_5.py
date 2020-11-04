list = []

y = 0
while y < 8:
    x = input('введи ' + str(y + 1) + '-e число: ')
    x = int(x)

    list.append(x)

    y += 1

print(list)


summa = 0
z = 0
while z < 8:
    summa = summa + list[z]
    z += 1

print(summa)