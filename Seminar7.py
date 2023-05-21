# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает. Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# # Ввод стихотворения
# poem = input('Enter a poem: ')

# # Разбиваем стихотворение на фразы и слова
# phrases = poem.split(' ')
# words_lists = list(map(lambda phrase: phrase.split('-'), phrases))
# print(words_lists)

# # Подсчитываем количество гласных букв в каждом слове
# counts_lists = list(map(lambda words: list(map(lambda word: sum(map(lambda letter: letter.lower() in 'aeiouy', word)), words)), words_lists))

# # Получаем список из количества гласных букв в каждой фразе
# counts = list(map(lambda count: sum(count), counts_lists))

# # Проверяем, есть ли ритм в каждой фразе
# rhythm = all(list(map(lambda count: count == counts[0], counts)))

# # Выводим результат
# if rhythm:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

#------------------------------------------------------------------------------------------------------------------------------------------------

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# operation = lambda row, col: row * col

# def print_operation_table(operation, num_rows=6, num_columns=6):

#     cell_width = len(str(operation(num_rows, num_columns))) + 1
#     print(' ' * cell_width, end='|')
    
#     for col in range(2, num_columns + 1):
#         print(str(col).rjust(cell_width), end='|')
#     print()
#     print('-' * ((cell_width + 1) * (num_columns + 1)))

#     for row in range(2, num_rows + 1):
#         print(str(row).rjust(cell_width), end='|')
#         for col in range(2, num_columns + 1):
#             print(str(operation(row, col)).rjust(cell_width), end='|')
#         print()

# # Тестируем функцию
# print_operation_table(operation)
