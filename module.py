def filter_by_condition(condition: bool, array: list) -> list:
    """
    Фильтрует массив по заданному условию в функции
    """
    result = []

    for element in array:
        if condition(element):
            result.append(element)

    return result


def for_each(function, array: list) -> list:
    """
    Принимает другую функцию и список,
    применяет функцию к каждому элементу списка
    и возвращает новый список
    """
    result = []

    for element in array:
        element = function(element)
        result.append(element)

    return result


def create_counter():
    """
    Функция-счётчик
    """
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter
