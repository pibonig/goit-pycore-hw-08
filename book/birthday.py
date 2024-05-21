from datetime import datetime

from book.field import Field


class Birthday(Field):
    def __init__(self, value):
        try:
            super().__init__(datetime.strptime(value, '%d.%m.%Y'))
        except ValueError:
            raise ValueError('Invalid date format. Use DD.MM.YYYY')

    def __repr__(self):
        return self.value.strftime('%d.%m.%Y')
