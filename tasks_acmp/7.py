"""
Решение задачи на ACMP.ru

Два бандита
https://acmp.ru/index.asp?main=task&id_task=33
"""

my_listin = []
my_list = []
bank = input()

my_listin = bank.split()

for i in my_listin:
    i = int(i)
    my_list.append(i)

summa_bank = (my_list[0] + my_list[1])

if my_list[0] == 0:
    G_not = my_list[1]
    L_not = my_list[0]
elif my_list[1] == 0:
    G_not = my_list[1]
    L_not = my_list[0]
elif summa_bank > 0:
    G_not = (summa_bank -1) - my_list[0]
    L_not = (summa_bank -1) - my_list[1]
elif summa_bank == 0:
    G_not = summa_bank - my_list[0]
    L_not = summa_bank - my_list[1]

print(G_not, L_not)

