import model

class PhonebookController:
    def __init__(self, phonebook):
        self.phonebook = phonebook

    def add_entry(self, name, surname, phone):
        entry = model.PhonebookEntry(name, surname, phone)
        self.phonebook.add_entry(entry)

    def remove_entry(self, entry):
        self.phonebook.remove_entry(entry)

    def search_entries(self, search_term):
        return self.phonebook.search_entries(search_term)
