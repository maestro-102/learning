"""
Решение задачи на ACMP.ru

Арифметика
https://acmp.ru/index.asp?main=task&id_task=8
"""

my_scroll = []
my_list = []
number = input()
my_scroll = number.split()

for i in my_scroll:
    i = int(i)
    my_list.append(i)

composition = my_list[0] * my_list[1]

if my_list[2] == composition:
    print('YES')
else:
    print('NO')
