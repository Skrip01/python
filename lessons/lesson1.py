# n = 1.89

# print(n)


# n = 'fddf'
# print(n)
# n1= "fddf"

# n = 5
# print(type(n))

# n = 'ssdsa'
# print(type(n))

# n = 'ss\'ds'
# print(n)

# n = 'sdsad"sdasd"asda'
# print(n)

# a = 5
# b = 5.89
# c = 'Hello'
# print(a,' - ', b, ' - ',c)

# a = 5
# b = 5.89
# c = 'Hello'
# print(f"{a} - {b} - {c}")

# a = 5
# b = 5.89
# c = 'Hello'
# print('{} - {} - {}'.format(a,b,c))

# print("Введите первое число: ")
# a = int(input())

# b = int(input('Введите второе число: '))

# print(f'Сумма {a} и {b} = {float(a) + float(b)}')

# c = 5.89
# print(c)
# print(type(c))
# n = int(c)
# print(n)
# print(type(n)) 

# c = 1
# print(c)
# print(type(c))
# n = bool(c)
# print(n)
# print(type(n)) 

# a = 5.864651
# b = 5.454665
# print(round(a*b, 3))

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a= 1 != 2
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = 1 < 3 < 5 < 10
# print(a)

# username = input('Ваше имя: ')
# if username == 'Маша':
#     print('Ура это же Маша')
# elif username == 'Марина':
#     print('Я так ждал вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print(f'Привет, {username}')

# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa += x
#     n //= 10
# print(summa)

# i = 0
# while i < 5:
#     if i ==3:
#         break
#     i += 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i += 1

# a = 'qwerty'

# for i in a:
#     print(i)

# line = ''
# for i in range(5):
#     line = ''
#     for j in range(5):
#         line += '*'
#     print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text))
# print('ещё' in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('ещё','ЕЩЁ'))

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])                                  # с
# print(text[1])                                  # ъ
# print(text[len(text)-1])                        # к
# print(text[-5])                                 # б
# print(text[:])                                  # съешь ещё мягких французских булок
# print(text[:2])                                 # съ
# print(text[len(text)-2:])                       # ок
# print(text[2:9])                                # ешь ещё
# print(text[6:-18])                              # ещё этих мягких
# print(text[0:len(text):6])                      # сеикакл
# print(text[::6])                                # сеикакл
# text = text[2:9] + text[-5] + text[:2]          # ешь ещёбсъ
# print(text)