class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        if self._is_valid_vin(vin):
            self._vin = vin
        if self._is_valid_number(numbers):
            self._numbers = numbers

    def _is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип VIN номера')
        if vin_number not in range(1000000, 9999999 + 1):
            raise IncorrectVinNumber('Неверный диапазон для VIN номера')

    def _is_valid_number(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Не корректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длинна номера')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'F123DJ')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'T001TP')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'Нет Номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
