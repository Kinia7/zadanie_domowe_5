class Field:        # Klasa bazowa, która ma jedynie pole 'value'
    def __init__(self, value=None):
        self.value=value

    def set_value(self, value):
        self.value = value

class Name(Field):  # Klasa dziedzicząca, przechowuje imię i nazwsko
    pass

class Phone(Field):  # Klasa dziedzicząca, przechowuje numer telefonu
    pass

class Record:       # reprezentuje wpis w książce adresowej
    def __init__(self, name):
        self.name = Name(name)   # 'name' który jest obiektem klasy Name
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break
    
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.set_value(new_phone)
                break

from collections import UserDict

class AddressBook(UserDict):  # 'AddressBook' reprezentuje samą ksiażkę adresową, dziedziczy z 'UserDict' co ułatwia zarządzanie danymi.
    def add_record(self, record):
        key = record.name.value
        self.data[key] = record

# Tworzymy nowy wpis
person = Record("Jan Kowalski")
person.add_phone("123-456-789")

# Tworzymy książkę adresową
address_book = AddressBook()
address_book.add_record(person)

# Pobieramy rekord z książki adresowej
jan_kowalski = address_book["Jan Kowalski"]

# Edytujemy numer telefonu
jan_kowalski.edit_phone("123-456-789", "987-654-321")

print(jan_kowalski.phones[0].value)
