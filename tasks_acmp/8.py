"""
Решение задачи на ACMP.ru

Зарплата
https://acmp.ru/index.asp?main=task&id_task=21
"""

my_scroll = []
my_list = []
money = input()
my_scroll = money.split()

for i in my_scroll:
    i = int(i)
    my_list.append(i)

if my_list[0] < my_list[1]:
    min = my_list[0]
else:
    min = my_list[1]
if min > my_list[2]:
    min = my_list[2]

if my_list[0] > my_list[1]:
    max = my_list[0]
else:
    max = my_list[1]
if max < my_list[2]:
    max = my_list[2]

difference = max - min

print(difference)
