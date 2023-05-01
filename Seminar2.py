# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

# N = int(input('Enter the number of coins '))
# orel = reshka = 0
# for i in range(N):
#     x = int(input('Heads(1) or tails(0)? '))
#     if x == 1:
#         orel += 1
#     else:
#         reshka += 1
# if orel < reshka:
#     print(f'Flip {orel}  coins from heads to tails, there are the least of them')
# elif orel == reshka:
#     print(f'The number of heads and tails is the same, {orel} pieces each')
# else:
#     print((f'Flip {reshka} coins from tails to heads, there are the least of them'))

#-----------------------------------------------------------------------------

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# x = abs(int(input('Enter the first natural1 number X from 1 to 1000 ')))
# y = abs(int(input('Enter the second natural number Y from 1 to 1000 ')))
# if x > 1 or x < 1000 or y > 1 or y < 1000:
#     print('You entered a number not from the specified range!')
# else:
#     S = x + y
#     P = x * y
#     stop = 0
#     for i in range(1001):
#         if stop != 1:
#             for j in range(1001):
#                 if stop != 1:
#                     if i * j == P and i + j == S:
#                         print(i, j)
#                         stop = 1
#             else:
#                 j = 1001
#         else:
#             i = 1001

# #-----------------------------------------------------------------------------

# # Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# # 10 -> 1 2 4 8

# N = abs(int(input('Enter a number N ')))
# stop = 0
# P = 2
# for i in range(N):
#     if stop != 1:
#         P = P ** i
#         if P <= N:
#             print(P, end=' ')
#             P = 2
#         else:
#             stop = 1
#     else:
#         i = N