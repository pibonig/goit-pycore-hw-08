import re

from book.field import Field


class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError('Invalid phone number format. Use XXXXXXXXXX')
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, phone_number):
        if not self.validate_phone(phone_number):
            raise ValueError('Invalid phone number format. Use XXXXXXXXXX')
        self.__value = phone_number

    @staticmethod
    def validate_phone(phone_number):
        return bool(re.fullmatch(r'\d{10}', phone_number))
