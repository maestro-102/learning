"""
Решение задачи на ACMP.ru

Больше-меньше
https://acmp.ru/index.asp?main=task&id_task=25
"""

number_a = input()
number_a = int(number_a)

number_b = input()
number_b = int(number_b)

if number_a < number_b:
    print('<')
elif number_a > number_b:
    print('>')
else:
    print('=')
