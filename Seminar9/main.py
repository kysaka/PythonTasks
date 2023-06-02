import os
import model
import controller
from view import PhonebookView
from text import *

def open_phonebook():
    filename = input(OPEN_PHONEBOOK_PROMPT)
    if os.path.exists(filename):
        with open(filename, 'r', encoding='cp1251') as file:
            phonebook_entries = file.readlines()
        phonebook = model.Phonebook()
        for entry in phonebook_entries:
            entry_data = entry.strip().split(":")
            if len(entry_data) == 3:
                name, surname, phone = entry_data
                phonebook.add_entry(model.PhonebookEntry(name.strip(), surname.strip(), phone.strip()))
        print(OPEN_SUCCESS_MSG)
        return phonebook
    else:
        print(FILE_NOT_FOUND_MSG)
        return model.Phonebook()

def save_phonebook(phonebook):
    filename = input(SAVE_PHONEBOOK_PROMPT)
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in phonebook.entries:
            file.write(str(entry) + "\n")
    print(SAVE_SUCCESS_MSG)

def add_entry(phonebook):
    name, surname, phone = PhonebookView.prompt_entry_details()
    controller.PhonebookController(phonebook).add_entry(name, surname, phone)
    PhonebookView.display_message(ADD_SUCCESS_MSG)

def delete_entry(phonebook):
    search_term = input(DELETE_ENTRY_PROMPT)
    entries_to_remove = controller.PhonebookController(phonebook).search_entries(search_term)
    if entries_to_remove:
        for entry in entries_to_remove:
            controller.PhonebookController(phonebook).remove_entry(entry)
        PhonebookView.display_message(DELETE_SUCCESS_MSG)
    else:
        PhonebookView.display_message(DELETE_NOT_FOUND_MSG)

def search_entries(phonebook):
    search_term = PhonebookView.prompt_search_term()
    found_entries = controller.PhonebookController(phonebook).search_entries(search_term)
    PhonebookView.display_entries(found_entries)

def main():
    phonebook = model.Phonebook()
    view = PhonebookView()
    while True:
        view.display_menu()
        choice = view.get_user_choice()
        if choice == "1":
            phonebook = open_phonebook()
        elif choice == "2":
            save_phonebook(phonebook)
        elif choice == "3":
            add_entry(phonebook)
        elif choice == "4":
            delete_entry(phonebook)
        elif choice == "5":
            search_entries(phonebook)
        elif choice == "6":
            break
        else:
            view.display_message(INVALID_CHOICE_MSG)

if __name__ == '__main__':
    main()
