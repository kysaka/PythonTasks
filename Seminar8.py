import os

# создаем функцию для записи данных в файл
def save_data(phonebook):
    filename = input("Введите название файла для сохранения (без расширения): ")
    try:
        with open(filename + ".txt", "w") as file:
            for contact in phonebook:
                file.write(contact["name"] + "," + contact["surname"] + "," + contact["phone"] + "\n")
        print(f"Справочник сохранен в файле {filename}.txt")
    except:
        print("Невозможно сохранить файл")

# создаем функцию для чтения данных из файла
def load_data():
    filename = input("Введите название файла для открытия (без расширения): ")
    try:
        with open(filename + ".txt", "r") as file:
            phonebook = []
            for line in file:
                data = line.strip().split(",")
                phonebook.append({"name":data[0], "surname":data[1], "phone":data[2]})
            print(f"Справочник загружен из файла {filename}.txt")
            return phonebook
    except:
        print("Невозможно открыть файл")

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

while True:
    print("""Меню:
1. Поиск контакта
2. Добавление контакта
3. Удаление контакта
4. Сохранение справочника
5. Выход""")
    choice = input("Выберите пункт меню: ")
    if choice == "1":
        find_contact(phonebook)
    elif choice == "2":
        add_contact(phonebook)
    elif choice == "3":
        delete_contact(phonebook)
    elif choice == "4":
        save_data(phonebook)
    elif choice == "5":
        exit_program()
    else:
        print("Неверный ввод") 