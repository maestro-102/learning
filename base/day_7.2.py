# Учительница дала Васе и Пете длинный список чисел.
# Вася и Петя должны найти:
# - сумму всех чисел
# - произведение всех чисел
# - разность всех чисел
# а также составить новый список из имеющегося, каждый элемент которого должен быть возведён в степень 3.
#
# Это уже не впервые, поэтому нужно помочь им составить программу, чтобы облегчить жизнь.
#
#
# Входные данные:
# 22, 11, 3, -4, 8, -1, 6, 96, 101
#
# Выходные данные:
# Сумма: 242
# Произведение: 1351544832
# Разность: -220
# Список в третьей степени: [10648, 1331, 27, -64, 512, -1, 216, 884736, 1030301]

my_list = [22, 11, 3, -4, 8, -1, 6, 96, 101]
my_listing = []

summa = 0
for i in my_list:
    summa = summa + i
print('сумма: ', summa)

multiple = 1
for i in my_list:
    multiple = multiple * i
print('произведение: ', multiple)

difference = my_list[0]
for i in my_list:
    difference = difference - i
print('разность: ', difference)

power = 1
for i in my_list:
        power = i ** 3
        my_listing.append(power)
print('список в степени: ', my_listing)
