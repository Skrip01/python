'''
1. Проверка четности числа
Напиши программу, которая запрашивает у пользователя число и определяет, является ли оно четным или нечетным.
'''
# number = int(input('Введите число: '))
# if number % 2 == 0:
#     print(f'Число {number} четное')
# else:
#     print(f'Число {number} нечетное')

'''
2. Подсчет слов в строке
Напиши программу, которая запрашивает у пользователя строку и подсчитывает количество слов в этой строк
'''
# text = input('Введите строку: ')
# word_count = len(text.split())
# print(f'Количество слов в строке - {word_count}')

'''
3. Калькулятор
Напиши простую программу-калькулятор, которая запрашивает у пользователя два числа и операцию (+, -, *, /), а затем выводит результат.
'''
# num1 = float(input('Введите первое число: '))
# num2 = float(input('Введите второе число: '))
# operation = input('Введите операцию (+, -, /, *): ')

# if operation == '+':
#     result = num1 + num2
# elif operation == '-':
#     result = num1 - num2
# elif operation == '/':
#     result = num1 / num2
# elif operation == '*':
#     result = num1 * num2
# else:
#     result = 'Неверная операция'
    
# print(f'Результат: {result}')

'''
4. Сумма чисел в списке
Напиши программу, которая запрашивает у пользователя список чисел и выводит их сумму.
'''

# numbers = input('Введите числа через пробел: ').split()
# numbers = [int(num) for num in numbers]
# total = sum(numbers)
# print(f'Сумма чисел: {total}')

'''
5. Поиск максимального и минимального числа
Напиши программу, которая запрашивает у пользователя список чисел и находит максимальное и минимальное число в этом списке.
'''
# numbers = input('Введите числа через пробел').split()
# numbers = [int(num) for num in numbers]
# max_num = max(numbers)
# min_num = min(numbers)
# print(f'Минимальное число: {min_num}')
# print(f'Максимальное число: {max_num}')

'''
6. Генератор паролей
Напиши программу, которая генерирует случайный пароль заданной длины, состоящий из букв, цифр и символов.
'''
# import random
# import string

# length = int(input("Введите длину пароля: "))
# characters = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choice(characters) for i in range(length))
# print(f"Сгенерированный пароль: {password}")

'''
7. Проверка на палиндром
Напиши программу, которая запрашивает у пользователя строку и проверяет, является ли она палиндромом (читается одинаково в обоих направлениях).
'''
# text = input('Введите слово: ')
# if text == text[::-1]:
#     print('Слово является палиндромом')
# else:
#     print('Слово не является палиндромом')
    
'''
10. Обратный отсчет
Напиши программу, которая запрашивает у пользователя число и выполняет обратный отсчет от этого числа до нуля с интервалом в одну секунду.
'''
# import time

# number = int(input("Введите число для обратного отсчета: "))
# while number >= 0:
#     print(number)
#     time.sleep(1)
#     number -= 1
# print("Обратный отсчет завершен!")

'''
11. Конвертер температуры
Напиши программу, которая конвертирует температуру из градусов Цельсия в градусы Фаренгейта.
'''
# celsius = float(input("Введите температуру в градусах Цельсия: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"Температура в градусах Фаренгейта: {fahrenheit}")

'''
12. Фибоначчи
Напиши программу, которая запрашивает у пользователя число n и выводит первые n чисел последовательности Фибоначчи
'''
# n = int(input("Введите количество чисел Фибоначчи: "))
# fib = [0, 1]

# for i in range(2, n):
#     next_number = fib[-1] + fib[-2]
#     fib.append(next_number)

# print(f"Первые {n} чисел Фибоначчи: {fib[:n]}")

'''
13. Анаграмма
Напиши программу, которая запрашивает у пользователя две строки и проверяет, являются ли они анаграммами (содержат ли они одинаковые буквы в одинаковом количестве, но в разном порядке).
'''
# str1 = input("Введите первую строку: ").lower()
# str2 = input("Введите вторую строку: ").lower()

# if sorted(str1) == sorted(str2):
#     print("Строки являются анаграммами")
# else:
#     print("Строки не являются анаграммами")

'''
14. Обратный порядок слов в строке
Напиши программу, которая запрашивает у пользователя строку и выводит слова в обратном порядке.
'''
# text = input("Введите строку: ")
# reversed_words = ' '.join(reversed(text.split()))
# print(f"Слова в обратном порядке: {reversed_words}")

'''
15. Калькулятор площади прямоугольника
Напиши программу, которая запрашивает у пользователя длину и ширину прямоугольника и вычисляет его площадь.
'''
# length = float(input("Введите длину прямоугольника: "))
# width = float(input("Введите ширину прямоугольника: "))
# area = length * width
# print(f"Площадь прямоугольника: {area}")

'''
16. Число в обратном порядке
Напиши программу, которая запрашивает у пользователя число и выводит его циф
'''
# number = input("Введите число: ")
# reversed_number = number[::-1]
# print(f"Число в обратном порядке: {reversed_number}")

'''
17. Количество гласных в строке
Напиши программу, которая запрашивает у пользователя строку и подсчитывает количество гласных букв (a, e, i, o, u) в этой строке.
'''
# text = input("Введите строку: ").lower()
# vowels = "уеыаоэяию"
# vowel_count = sum(1 for char in text if char in vowels)
# print(f"Количество гласных в строке: {vowel_count}")
