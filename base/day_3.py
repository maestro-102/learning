x = input('введите число: ')
x = int(x)

y = input('введите следующее число: ')
y = int(y)

z = input('введите знак математического действия: ')


if z == '+':
    print(x + y)
elif z == '-':
    print(x - y)
elif z == '*':
    print(x * y)
elif z == '/':
    if y == 0:
        print('НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ')
    else:
        print(x / y)
else:
    print('Неизестная операция...')


if x != 0 and y != 0:
    print('X и Y не равны нулю...')
