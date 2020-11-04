"""
Решение задачи на ACMP.ru

Эния
https://acmp.ru/index.asp?main=task&id_task=195
"""

# вес = 1 нгр/кв.м
my_list_panel = []
panel = input()
my_list = panel.split()

for i in my_list:
    i = int(i)
    my_list_panel.append(i)

volume = (my_list_panel[0] * my_list_panel[1] * 2 * my_list_panel[2]) * 1
print (volume)