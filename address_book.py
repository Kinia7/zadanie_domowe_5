class Field:       
    def __init__(self, value=None):
        self.value=value

    def set_value(self, value):
        self.value = value

class Name(Field):  
    pass

class Phone(Field):  
    pass

class Record:       
    def __init__(self, name):
        self.name = Name(name)  
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

class AddressBook(UserDict):  
    def add_record(self, record):
        key = record.name.value
        self.data[key] = record


person = Record("Jan Kowalski")
person.add_phone("123-456-789")


address_book = AddressBook()
address_book.add_record(person)


jan_kowalski = address_book["Jan Kowalski"]

# Edytujemy numer telefonu
jan_kowalski.edit_phone("123-456-789", "987-654-321")

print(jan_kowalski.phones[0].value)
