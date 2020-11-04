stop_words = ('apple', 'meloy', 'chery')
my_list = []

while True:
    user_in = input('ввести слово: ')

    if user_in in stop_words:
        break
    else:
        my_list.append(user_in)

print(my_list)
