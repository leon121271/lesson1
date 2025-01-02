def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчета суммы - {i}')

    return result, incorrect_data

def calculate_average(numbers):
    try:
        if isinstance(numbers, (int, float)):
            raise TypeError('некорректный тип данных')
        if isinstance(numbers, str):
            numbers = list(numbers)
        result, incorrect_count = personal_sum(numbers)

        average = result / (len(numbers) - incorrect_count)
        return average

    except ZeroDivisionError:
        return 0
    except TypeError as exc:
        print(f'В numbers записан {exc}')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Еще Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')

