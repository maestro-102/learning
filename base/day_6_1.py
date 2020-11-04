my_list = []

number_for_break = input('какое ввести число? ')
number_for_break = int(number_for_break)

for i in range(10):
    user_number = input('ввести число: ')
    user_number = int(user_number)
    my_list.append(user_number)

summa = 0
for i in my_list:
    if i == number_for_break:
        break
    if i >= 0:
       summa = summa + i


print(summa)
