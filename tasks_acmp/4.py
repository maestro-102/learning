"""
Решение задачи на ACMP.ru

Орешки
https://acmp.ru/index.asp?main=task&id_task=766
"""

my_list_int = []
number = input()
my_list = number.split()

for i in my_list:
    i = int(i)
    my_list_int.append(i)

composition = my_list_int[0] * my_list_int[1]

if composition < my_list_int[2]:
    print('NO')
elif composition >= my_list_int[2]:
    print('YES')
