"""
Решение задачи на ACMP.ru

Гулливер
https://acmp.ru/index.asp?main=task&id_task=773
"""

my_list = []
my_listin = []
mattress = input()
my_list = mattress.split()

for i in my_list:
    i = int(i)
    my_listin.append(i)

size = (my_listin[0] ** 2) * my_listin[1]
print(size)
