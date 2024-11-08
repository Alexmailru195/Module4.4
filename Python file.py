def example_function(*args, **kwargs):
    """args - это кортеж, который может принимать любое количество позиционных аргументов"""
    print("Args:", args)

    """kwargs - это словарь, который может принимать любое количество именованных аргументов"""
    print("Kwargs:", kwargs)

"""Пример использования функции с разными аргументами"""
example_function(1, 2, 3)
"""Вывод: Args: (1, 2, 3) | Kwargs: {}"""

example_function(1, 2, name="Александр", age=23)
"""Вывод: Args: (1, 2) | Kwargs: {'name': 'Александр', 'age': 23}"""

def sum_numbers(*args):
    """Подсчитываем сумму всех переданных чисел"""
    return sum(args)

print(sum_numbers(1, 2, 3, 4))
"""Вывод: 10"""

def introduce(**kwargs):
    """Выводим информацию"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

introduce(name="Александр", occupation="Программист")
"""Вывод: name: Александр | occupation: Программист"""