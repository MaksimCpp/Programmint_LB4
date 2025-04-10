from functools import reduce
from random import randint

from module import filter_by_condition, for_each, create_counter

ARRAY_LENGTH = 20
START_VALUE = 1
END_VALUE = 100

print("\n1) Часть А\n2) Часть Б\n3) Часть В\n4) Часть Г\n5) Выход")
choice = int(input("\nВыберите действие: "))

while choice != 5:
    if choice == 1:
        array = [randint(START_VALUE, END_VALUE) for _ in range(ARRAY_LENGTH)]
        result = filter_by_condition(lambda x: x % 2 == 0, array)

        print(f'\nИсходный массив:\n{array}')
        print(f'\nРезультат:\n{result}\n')

    elif choice == 2:
        array = [randint(START_VALUE, END_VALUE) for _ in range(ARRAY_LENGTH)]
        result = for_each(lambda x: x * 2, array)

        print(f'\nИсходный массив:\n{array}')
        print(f'\nРезультат:\n{result}')

    elif choice == 3:
        counter = create_counter()
        print(counter())
        print(counter())
        print(counter())

    elif choice == 4:
        array = [randint(START_VALUE, END_VALUE) for _ in range(ARRAY_LENGTH)]
        result = reduce(lambda x, y: x + y, array)

        print(f'\nИсходный массив:\n{array}')
        print(f'\nРезультат:\n{result}')

    print("\n1) Часть А\n2) Часть Б\n3) Часть В\n4) Часть Г\n5) Выход")
    choice = int(input("\nВыберите действие: "))
