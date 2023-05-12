# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

# def power(a, b):
#     if b == 0:
#         return 1
#     elif b % 2 == 0:
#         return power(a * a, b // 2)
#     else:
#         return a * power(a, b - 1)

# a = int(input("Enter a number A: "))
# b = int(input("Enter a number B: "))

# print(power(a, b))

# Мне больше нравиться когда числа находятся рандомно и когда программа работает почтимю без участия пользователя. 

# import random

# def power(a, b):
#     if b == 0:
#         return 1
#     elif b % 2 == 0:
#         return power(a * a, b // 2)
#     else:
#         return a * power(a, b - 1)

# a = random.randint(1, 10)
# b = random.randint(1, 5)

# print("Number A =", a)
# print("Number B =", b)

# print(power(a, b))

#-------------------------------------

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

import random

def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a + 1, b - 1)

# Генерируем случайные числа
a = random.randint(1, 10)
b = random.randint(1, 10)

print("Число A =", a)
print("Число B =", b)

print("Сумма =", sum(a, b))