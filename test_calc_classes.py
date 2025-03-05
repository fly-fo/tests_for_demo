import allure
import pytest
import random
from calc_classes import Calc

# в данном примере тестируем класс Calc

# создадим список случайных ошибок
ERROR_TYPES = [IndexError, ValueError, TypeError, KeyError]

# тестируем операцию сложения
# добавим набор параметров для нескольких тестов
# три пары параметров и ожидаемый результат
@pytest.mark.parametrize('a, b, expected', [
    (1, 9, 10),
    (2, 8, 10),
    (3, 'two', 5) # эта комбинация всегда падает
])
@allure.description('Этот тест проверяет операцию сложения.')
@allure.title('Проверка операции сложения.')
def test_addition(a, b, expected):
    # добавляем первый шаг, создание класса калькулятора и проверяем что он создался
    with allure.step('Шаг 1: Создание объекта класса калькулятора.'):
        with open('img/logo.jpeg', 'rb') as image_file:
            allure.attach(
                image_file.read(),
                name='ТестОпс Лого.jpg',
                attachment_type=allure.attachment_type.JPG
            )
        local_calc = Calc()
        assert isinstance(local_calc, Calc)
    # Добавляем шаг 2, с вложением текст
    with allure.step('Шаг 2: Проверяем начальное значение калькулятора.'):
        allure.attach(f'Создан калькулятор, начальное значение {local_calc.result}.', name='Лог операции', attachment_type=allure.attachment_type.TEXT)
        assert local_calc.result == 0, f'Crit Error: Экземпляр класса не создался.'
    # Добавляем шаг 3, само действие сложения
    with allure.step('Шаг 3: Проверяем выполняется ли сложение.'):
        # Добавляем шаг 3.1, шанс срабатывания калькулятора
        with allure.step('Шаг 3.1: Шанс срабатывания сложения 95%.'):
            if random.random() < 0.95:  # 95% шанс произвести операцию сложения
                local_calc.addition(a, b)
        # Добавляем шаг 3.2, проверка работы сложения
        with allure.step('Шаг 3.2: Проверяем действие сложения.'):
            allure.attach(f'Калькулятор {local_calc} произвел операцию сложения переменных {a} и {b}, в результате получили {local_calc.result}.',
                          name='Лог операции сложения', attachment_type=allure.attachment_type.TEXT)
            assert local_calc.result == expected, f'Crit Error: Сложение не произошло, или прошло некорректно. Параметры объекта {local_calc} неверное значение результата.'
    # Добавляем шаг 4, со случайной ошибкой
    with allure.step('Шаг 4: Шаг со случайной ошибкой.'):
        # Вставляем случайную ошибку, это приведет к сломанному тесту
        if random.random() < 0.2:  # 20% шанс на ошибку
            error_type = random.choice(ERROR_TYPES)  # случайно выбираем тип ошибки
            raise error_type(f'Случайная ошибка: {error_type.__name__}')



# тестируем операцию вычитания
# добавим набор параметров для нескольких тестов
# три пары параметров и ожидаемый результат
@pytest.mark.parametrize('a, b, expected', [
    (9, 1, 8),
    (8, 2, 6),
    (7, 'two', 5) # эта комбинация всегда падает
])
@allure.description('Этот тест проверяет операцию вычитания.')
@allure.title('Проверка операции вычитания.')
def test_subtraction(a, b, expected):
    # добавляем первый шаг, создание класса калькулятора и проверяем что он создался
    with allure.step('Шаг 1: Создание объекта класса калькулятора.'):
        with open('img/logo.jpeg', 'rb') as image_file:
            allure.attach(
                image_file.read(),
                name='ТестОпс Лого.jpg',
                attachment_type=allure.attachment_type.JPG
            )
        local_calc = Calc()
        assert isinstance(local_calc, Calc)
    # Добавляем шаг 2, с вложением текст
    with allure.step('Шаг 2: Проверяем начальное значение калькулятора.'):
        allure.attach(f'Создан калькулятор, начальное значение {local_calc.result}.', name='Лог операции', attachment_type=allure.attachment_type.TEXT)
        assert local_calc.result == 0, f'Crit Error: Экземпляр класса не создался.'
    # Добавляем шаг 3, само действие вычитания
    with allure.step('Шаг 3: Проверяем выполняется ли вычитание.'):
        # Добавляем шаг 3.1, шанс срабатывания калькулятора
        with allure.step('Шаг 3.1: Шанс срабатывания вычитания 95%.'):
            if random.random() < 0.95:  # 95% шанс произвести операцию вычитания
                local_calc.subtraction(a, b)
        # Добавляем шаг 3.2, проверка работы вычитания
        with allure.step('Шаг 3.2: Проверяем действие вычитания.'):
            allure.attach(f'Калькулятор {local_calc} произвел операцию вычитаниях: из переменной {a} вычитаем переменную {b}, в результате получили {local_calc.result}.',
                          name='Лог операции вычитания', attachment_type=allure.attachment_type.TEXT)
            assert local_calc.result == expected, f'Crit Error: Вычитание не произошло, или прошло некорректно. Параметры объекта {local_calc} неверное значение результата.'
    # Добавляем шаг 4, со случайной ошибкой
    with allure.step('Шаг 4: Шаг со случайной ошибкой.'):
        # Вставляем случайную ошибку, это приведет к сломанному тесту
        if random.random() < 0.2:  # 20% шанс на ошибку
            error_type = random.choice(ERROR_TYPES)  # случайно выбираем тип ошибки
            raise error_type(f'Случайная ошибка: {error_type.__name__}')

# тестируем операцию умножения
# добавим набор параметров для нескольких тестов
# три пары параметров и ожидаемый результат
@pytest.mark.parametrize('a, b, expected', [
    (0, 10, 0),
    (8, 2, 16),
    (7, 'two', 14) # эта комбинация всегда падает
])
@allure.description('Этот тест проверяет операцию умножения.')
@allure.title('Проверка операции умножения.')
def test_multiplication(a, b, expected):
    # добавляем первый шаг, создание класса калькулятора и проверяем что он создался
    with allure.step('Шаг 1: Создание объекта класса калькулятора.'):
        with open('img/logo.jpeg', 'rb') as image_file:
            allure.attach(
                image_file.read(),
                name='ТестОпс Лого.jpg',
                attachment_type=allure.attachment_type.JPG
            )
        local_calc = Calc()
        assert isinstance(local_calc, Calc)
    # Добавляем шаг 2, с вложением текст
    with allure.step('Шаг 2: Проверяем начальное значение калькулятора.'):
        allure.attach(f'Создан калькулятор, начальное значение {local_calc.result}.', name='Лог операции', attachment_type=allure.attachment_type.TEXT)
        assert local_calc.result == 0, f'Crit Error: Экземпляр класса не создался.'
    # Добавляем шаг 3, само действие умножения
    with allure.step('Шаг 3: Проверяем выполняется ли умножения.'):
        # Добавляем шаг 3.1, шанс срабатывания калькулятора
        with allure.step('Шаг 3.1: Шанс срабатывания умножения 95%.'):
            if random.random() < 0.95:  # 95% шанс произвести операцию умножения
                local_calc.multiplication(a, b)
        # Добавляем шаг 3.2, проверка работы умножения
        with allure.step('Шаг 3.2: Проверяем действие умножения.'):
            allure.attach(f'Калькулятор {local_calc} произвел операцию умножения: из переменной {a} вычитаем переменную {b}, в результате получили {local_calc.result}.',
                          name='Лог операции умножения', attachment_type=allure.attachment_type.TEXT)
            assert local_calc.result == expected, f'Crit Error: Умножение не произошло, или прошло некорректно. Параметры объекта {local_calc} неверное значение результата.'
    # Добавляем шаг 4, со случайной ошибкой
    with allure.step('Шаг 4: Шаг со случайной ошибкой.'):
        # Вставляем случайную ошибку, это приведет к сломанному тесту
        if random.random() < 0.2:  # 20% шанс на ошибку
            error_type = random.choice(ERROR_TYPES)  # случайно выбираем тип ошибки
            raise error_type(f'Случайная ошибка: {error_type.__name__}')

# тестируем операцию деления
# добавим набор параметров для нескольких тестов
# три пары параметров и ожидаемый результат
@pytest.mark.parametrize('a, b, expected', [
    (10, 0, 0), # эта комбинация всегда падает
    (8, 2, 4),
    (14, 'two', 2) # эта комбинация всегда падает
])
@allure.description('Этот тест проверяет операцию деления.')
@allure.title('Проверка операции деления.')
def test_division(a, b, expected):
    # добавляем первый шаг, создание класса калькулятора и проверяем что он создался
    with allure.step('Шаг 1: Создание объекта класса калькулятора.'):
        with open('img/logo.jpeg', 'rb') as image_file:
            allure.attach(
                image_file.read(),
                name='ТестОпс Лого.jpg',
                attachment_type=allure.attachment_type.JPG
            )
        local_calc = Calc()
        assert isinstance(local_calc, Calc)
    # Добавляем шаг 2, с вложением текст
    with allure.step('Шаг 2: Проверяем начальное значение калькулятора.'):
        allure.attach(f'Создан калькулятор, начальное значение {local_calc.result}.', name='Лог операции', attachment_type=allure.attachment_type.TEXT)
        assert local_calc.result == 0, f'Crit Error: Экземпляр класса не создался.'
    # Добавляем шаг 3, само действие деления
    with allure.step('Шаг 3: Проверяем выполняется ли деления.'):
        # Добавляем шаг 3.1, шанс срабатывания калькулятора
        with allure.step('Шаг 3.1: Шанс срабатывания деления 95%.'):
            if random.random() < 0.95:  # 95% шанс произвести операцию деления
                local_calc.division(a, b)
        # Добавляем шаг 3.2, проверка работы деления
        with allure.step('Шаг 3.2: Проверяем действие деления.'):
            allure.attach(f'Калькулятор {local_calc} произвел операцию деления: из переменной {a} вычитаем переменную {b}, в результате получили {local_calc.result}.',
                          name='Лог операции деления', attachment_type=allure.attachment_type.TEXT)
            assert local_calc.result == expected, f'Crit Error: Деления не произошло, или прошло некорректно. Параметры объекта {local_calc} неверное значение результата.'
    # Добавляем шаг 4, со случайной ошибкой
    with allure.step('Шаг 4: Шаг со случайной ошибкой.'):
        # Вставляем случайную ошибку, это приведет к сломанному тесту
        if random.random() < 0.2:  # 20% шанс на ошибку
            error_type = random.choice(ERROR_TYPES)  # случайно выбираем тип ошибки
            raise error_type(f'Случайная ошибка: {error_type.__name__}')