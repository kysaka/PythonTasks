class PhonebookEntry:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.surname}: {self.phone}"


class Phonebook:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def remove_entry(self, entry):
        self.entries.remove(entry)

    def search_entries(self, search_term):
        found_entries = []
        for entry in self.entries:
            if search_term in entry.name or search_term in entry.surname or search_term in entry.phone:
                found_entries.append(entry)
        return found_entries
