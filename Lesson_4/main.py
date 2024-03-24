'''
    Змінити функцію таким чином, щоб при введенні некорректного
    числа функція виводила повідомлення про те, що були введені
    некоректні дані і дати можливість ввести число ще раз. Повторювати
    це до тих пір, доки користувач не введе коректне число.
'''
def input_int(message):
    while True:
        result = int(input(message))
        return result


number = input_int('Введіть число: ')
print(number)


exit()

while True:
    a = input_int('Введіть перше число: ')
    b = input_int('Введіть друге число: ')

    try:
        print(f'{a} / {b} = {a/b}')
    except ZeroDivisionError:
        print('Ділити на нуль не можна!')
    except TypeError:
        print('Передано некоректні дані!')
    except Exception:
        print('Щось пішло не так!')
    else:
        break


print('END OF PROGRAM')