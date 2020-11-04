# debug_list = [1, 2, -3, -4, 0, 6, 7]

while True:
    x = input('введи число: ')
    x = int(x)

    if x == 0:
        break
    if x < 0:
        continue
    else:
        print(x + 10)


print('конец')
