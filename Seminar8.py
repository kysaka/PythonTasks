import os

# создаем функцию для записи данных в файл
def save_data(phonebook):
    filename = ("Справочник.txt")
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for contact in phonebook:
                file.write(contact["name"] + "," + contact["surname"] + "," + contact["phone"] + "\n")
        print("Телефонный справочник успешно сохранен.")
    except:
        print("Невозможно сохранить файл")

    
    #     file.writelines(phonebook)
    # print("Телефонный справочник успешно сохранен.")

# создаем функцию для чтения данных из файла
def load_data():
    filename = ("Справочник.txt")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print("Телефонный справочник успешно открыт.")
        return phonebook
    else:
        print("Файл не существует. Создайте новый справочник.")
        return []

# создаем функцию для поиска контакта
def find_contact(phonebook):
    search_str = input("Введите имя, фамилию или номер телефона для поиска: ")
    results = []
    for contact in phonebook:
        if search_str.lower() in (contact["name"] + " " + contact["surname"] + " " + contact["phone"]).lower():
            results.append(contact)
    if len(results) == 0:
        print("Контакты не найдены")
    else:
        print(f"Найдено контактов: {len(results)}")
        for contact in results:
            print(f"{contact['name']} {contact['surname']}: {contact['phone']}")

# создаем функцию для добавления контакта
def add_contact(phonebook):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    phonebook.append({"name":name, "surname":surname, "phone":phone})
    print("Контакт успешно добавлен")

# создаем функцию для удаления контакта
def delete_contact(phonebook):
    search_str = input("Введите имя, фамилию или номер телефона для удаления: ")
    results = []
    for contact in phonebook:
        if search_str.lower() in (contact["name"] + " " + contact["surname"] + " " + contact["phone"]).lower():
            results.append(contact)
    if len(results) == 0:
        print("Контакты не найдены")
    else:
        print(f"Найдено контактов: {len(results)}")
        for contact in results:
            phonebook.remove(contact)
        print(f"Контактов удалено: {len(results)}")

# создаем функцию для выхода из программы
def exit_program():
    print("До свидания")
    exit()

# основная программа
phonebook = []

# проверяем наличие файла с данными
if os.path.isfile("phonebook.txt"):
    phonebook = load_data()

def main():
    phonebook = []
    while True:
        print("\nТелефонный справочник")
        print("1. Открыть справочник")
        print("2. Сохранить справочник")
        print("3. Добавить запись")
        print("4. Удалить запись")
        print("5. Поиск записей")
        print("6. Выйти из программы")
        
        choice = input("Введите номер операции: ")
        
        if choice == "1":
            phonebook = load_data()
        elif choice == "2":
            save_data(phonebook)
        elif choice == "3":
            add_contact(phonebook)
        elif choice == "4":
            delete_contact(phonebook)
        elif choice == "5":
            find_contact(phonebook)
        elif choice == "6":
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите номер операции от 1 до 6.")

if __name__ == '__main__':
    main()

# import os

# def open_phonebook():
#     filename = input("Введите имя файла: ")
#     if os.path.exists(filename):
#         with open(filename, 'r') as file:
#             phonebook = file.readlines()
#         print("Телефонный справочник успешно открыт.")
#         return phonebook
#     else:
#         print("Файл не существует. Создайте новый справочник.")
#         return []

# def save_phonebook(phonebook):
#     filename = input("Введите имя файла для сохранения: ")
#     with open(filename, 'w', encoding='utf-8') as file:
#         file.writelines(phonebook)
#     print("Телефонный справочник успешно сохранен.")

# def add_entry(phonebook):
#     name = input("Введите имя: ")
#     surname = input("Введите фамилию: ")
#     phone = input("Введите номер телефона: ")
#     entry = f"{name} {surname}: {phone}\n"
#     phonebook.append(entry)
#     print("Запись успешно добавлена.")

# def delete_entry(phonebook):
#     search_term = input("Введите имя, фамилию или номер телефона для удаления: ")
#     entries_to_remove = []
#     for entry in phonebook:
#         if search_term in entry:
#             entries_to_remove.append(entry)
#     if entries_to_remove:
#         for entry in entries_to_remove:
#             phonebook.remove(entry)
#         print("Записи успешно удалены.")
#     else:
#         print("Записей не найдено.")

# def search_entries(phonebook):
#     search_term = input("Введите имя, фамилию или номер телефона для поиска: ")
#     found_entries = []
#     for entry in phonebook:
#         if search_term in entry:
#             found_entries.append(entry)
#     if found_entries:
#         print("Найденные записи:")
#         for entry in found_entries:
#             print(entry)
#     else:
#         print("Записей не найдено.")

# def main():
#     phonebook = []
#     while True:
#         print("\n Телефонный справочник")
#         print("1. Открыть справочник")
#         print("2. Сохранить справочник")
#         print("3. Добавить запись")
#         print("4. Удалить запись")
#         print("5. Поиск записей")
#         print("6. Выйти из программы")
        
#         choice = input("Введите номер операции: ")
        
#         if choice == "1":
#             phonebook = open_phonebook()
#         elif choice == "2":
#             save_phonebook(phonebook)
#         elif choice == "3":
#             add_entry(phonebook)
#         elif choice == "4":
#             delete_entry(phonebook)
#         elif choice == "5":
#             search_entries(phonebook)
#         elif choice == "6":
#             break
#         else:
#             print("Неверный ввод. Пожалуйста, выберите номер операции от 1 до 6.")