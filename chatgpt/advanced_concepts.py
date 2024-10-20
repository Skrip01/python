'''
1. Объектно-ориентированное программирование (ООП)
ООП является важным аспектом Python и включает в себя создание классов и объектов для моделирования реальных сущностей.


Классы и объекты
Класс — это шаблон для создания объектов. Объект — это экземпляр класса.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} говорит: Гав-гав")

# Создание объектов (экземпляров класса)
dog1 = Dog("Барбос", 3)
dog2 = Dog("Шарик", 5)

# Вызов методов объекта
dog1.bark()  # Выводит "Барбос говорит: Гав-гав"
dog2.bark()  # Выводит "Шарик говорит: Гав-гав"


Наследование
Наследование позволяет одному классу (подклассу) наследовать атрибуты и методы другого класса (родительского класса).

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} говорит: Мяу-мяу")

dog = Dog("Барбос")
cat = Cat("Мурка")

dog.make_sound()  # Выводит "Барбос говорит: Гав-гав"
cat.make_sound()  # Выводит "Мурка говорит: Мяу-мяу"


Полиморфизм
Полиморфизм позволяет использовать один интерфейс для различных типов данных.

def make_animal_sound(animal):
    animal.make_sound()

make_animal_sound(dog)  # Выводит "Барбос говорит: Гав-гав"
make_animal_sound(cat)  # Выводит "Мурка говорит: Мяу-мяу"


Инкапсуляция и абстракция
Инкапсуляция скрывает внутренние детали реализации, предоставляя доступ только к определённым методам.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Приватный атрибут

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Выводит 1300


2. Модули и пакеты
Модули
Модули — это файлы с расширением .py, содержащие код Python. Они позволяют организовать код в логические части и повторно использовать его.

# В файле my_module.py
def greet(name):
    return f"Hello, {name}!"

# В основном файле
import my_module

print(my_module.greet("Alice"))  # Выводит "Hello, Alice!"


Пакеты
Пакеты — это каталоги, содержащие модули и файл __init__.py.

# Структура пакета
# my_package/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# В файле __init__.py можно импортировать модули пакета
from .module1 import func1
from .module2 import func2

# В основном файле
import my_package

my_package.func1()
my_package.func2()


3. Обработка исключений
Обработка исключений позволяет управлять ошибками, которые могут возникнуть во время выполнения программы.

try:
    x = int(input("Введите число: "))
    result = 10 / x
except ValueError:
    print("Ошибка: введено не число")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
else:
    print(f"Результат: {result}")
finally:
    print("Блок finally выполнен в любом случае")
    
    
Создание пользовательских исключений

class CustomError(Exception):
    pass

def risky_function(x):
    if x < 0:
        raise CustomError("x не должно быть отрицательным")

try:
    risky_function(-1)
except CustomError as e:
    print(e)
    
    
4. Стандартная библиотека
Работа с датой и временем

import datetime

now = datetime.datetime.now()
print(now)  # Текущие дата и время

date_str = "2023-07-14"
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print(date_obj)  # Преобразование строки в дату

Регулярные выражения

import re

pattern = r"\d+"  # Шаблон для поиска цифр
text = "У меня 2 яблока и 3 апельсина"

matches = re.findall(pattern, text)
print(matches)  # Выводит ['2', '3']

Многопоточность и многопроцессорность
Многопоточность:

import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

Многопроцессорность:

import multiprocessing

def print_numbers():
    for i in range(5):
        print(i)

process = multiprocessing.Process(target=print_numbers)
process.start()
process.join()

Заключение
Эти продвинутые концепции помогут вам более глубоко понять Python и научат вас писать более эффективный, структурированный и надежный код. Практика и изучение этих тем сделают вас более уверенным разработчиком и приблизят вас к уровню middle.
'''