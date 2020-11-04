my_dict = {}

while True:
    key = input('ввести ключ: ')
    value = input('ввести значение: ')

    if key == '0':
        break
    elif value == '0':
        break
    else:
        my_dict[key] = value

print(my_dict)
