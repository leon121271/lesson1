def add_everything_up(a, b):
    try:
        if not isinstance(a, (int, float, str)) or not isinstance(b, (int, float, str)):
            raise ValueError('Недопустимый тип данных')
        return a + b
    except TypeError:
        return str(a) + str(b)
    except ValueError as exc:
        return f'Ошибка: {exc}'



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up([1, 2, 3], 5))