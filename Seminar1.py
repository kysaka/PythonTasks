# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# number = input("Введите трехзначное число: ")

# # Проверяем, что пользователь ввел трехзначное число
# if len(number) != 3:
#     print("Ошибка! Нужно ввести трехзначное число.")
# else:
#     digit1 = int(number[0])
#     digit2 = int(number[1])
#     digit3 = int(number[2])

#     sum = digit1 + digit2 + digit3

#     print(f"Сумма цифр числа {number} = {sum}")

# ---------------------------------------------------

# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# number = input("Введите общее количество журавликов: ")
# kate = int(number) / 2
# petyansergey = int(kate) / 2

# print(f"Катя сделала {int(kate)} журавликов. Петя и Сережа сделали по {int(petyansergey)} журавликов.")

# --------------------------------------------------------------------------------------------------------