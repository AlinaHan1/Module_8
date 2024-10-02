def personal_sum(*numbers):  # принимает коллекцию
    result = 0
    incorrect_data = 0
    for i in numbers:  # перебор коллекции
        for j in i:
            try:
                result += j
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчета суммы - {j}')
    return result, incorrect_data


def calculate_average(*numbers):
    if isinstance(*numbers, int):
        return None
    try:
        tp_sum = personal_sum(*numbers)
        return tp_sum[0] / (len(*numbers) - tp_sum[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        return f'В numbers записан не корректный тип данных'


print(f'Результат 1:{calculate_average("1, 2, 3")}')  # строка перебирается, но каждый символ строковый
print(f'Результат 2:{calculate_average([1, "Строка", 3, "Еще строка"])}')  # Учитывается только 1 и 3
print(f'Результат 3:{calculate_average(567)}')  # передана не коллекция
print(f'Результат 4:{calculate_average([42, 15, 36, 13])}')
