from collections import UserDict

from book.record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        return [{
            'name': record.name,
            'birthday': record.birthday
        } for record in self.data.values() if record.is_birthday_upcoming()]
