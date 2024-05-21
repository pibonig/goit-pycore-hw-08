from datetime import datetime, timedelta

from book.birthday import Birthday
from book.name import Name
from book.phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                break

    def edit_phone(self, old_phone_number, new_phone_number):
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone.value = new_phone_number
                return

        raise ValueError('Phone not found.')

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def is_birthday_upcoming(self):
        if self.birthday is not None:
            now = datetime.now().date()
            user_birthday = self.birthday.value.date()
            user_birthday_this_year = user_birthday.replace(year=now.year)

            if user_birthday_this_year < now:
                user_birthday_this_year = user_birthday_this_year.replace(year=now.year + 1)

            days_to_user_birthday = (user_birthday_this_year - now).days

            if 0 <= days_to_user_birthday <= 7:
                weekday = user_birthday_this_year.weekday()
                if weekday >= 5:
                    user_birthday_this_year += timedelta(days=7 - weekday)

                return True

        return False

    def __str__(self):
        data = [f"Contact name: {self.name.value}"]

        if self.phones:
            data.append(f"Phones: {', '.join(p.value for p in self.phones)}")

        if self.birthday is not None:
            data.append(f"Birthday: {self.birthday.value}")

        return '; '.join(data)
