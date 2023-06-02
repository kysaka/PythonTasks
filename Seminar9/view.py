from text import *

class PhonebookView:
    @staticmethod
    def display_menu():
        print("\nТелефонный справочник")
        print("1. Открыть справочник")
        print("2. Сохранить справочник")
        print("3. Добавить запись")
        print("4. Удалить запись")
        print("5. Поиск записей")
        print("6. Выйти из программы")

    @staticmethod
    def get_user_choice():
        return input("Введите номер операции: ")

    @staticmethod
    def prompt_entry_details():
        name = input(ADD_ENTRY_PROMPT)
        surname = input(ADD_SURNAME_PROMPT)
        phone = input(ADD_PHONE_PROMPT)
        return name, surname, phone

    @staticmethod
    def prompt_search_term():
        return input(SEARCH_ENTRY_PROMPT)

    @staticmethod
    def display_entries(entries):
        if entries:
            print(SEARCH_FOUND_MSG)
            for entry in entries:
                print(entry)
        else:
            print(SEARCH_NOT_FOUND_MSG)

    @staticmethod
    def display_message(message):
        print(message)
