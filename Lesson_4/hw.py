result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, '': 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
    except (ValueError, IndexError, TypeError, ZeroDivisionError) as error:
        print('Помилка:', error)
    else:
        result.append(res)

print(result)