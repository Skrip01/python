# Задача №1. По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

# n = 5
# result = 1
# i = 0
# while i < n:
#     result *= (i + 1)
#     i += 1
# print(result)


# Задача №2. Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1


# Задача №3. Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50

# Ввод данных
# N = int(input("Введите количество дней (1 ≤ N ≤ 100): "))
# temperatures = list(map(int, input("Введите температуры через пробел: ").split()))

# max_thaw_length = 0
# current_thaw_length = 0

# # Проход по всем температурам
# for temp in temperatures:
#     if temp > 0:
#         current_thaw_length += 1
#         if current_thaw_length > max_thaw_length:
#             max_thaw_length = current_thaw_length
#     else:
#         current_thaw_length = 0

# print("Длина самой длинной оттепели:", max_thaw_length)

# Задача №4.Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# N = [5 , 1 , 6, 5, 9]
# print(min(N),max(N))

# Варианнт 2

# N = [5 , 1 , 6, 5, 9]

# min_weight = N[0]
# max_weight = N[0]

# for weight in N:
#     if weight < min_weight:
#         min_weight = weight
#     if weight > max_weight:
#         max_weight = weight
# print(min_weight,max_weight)
        



