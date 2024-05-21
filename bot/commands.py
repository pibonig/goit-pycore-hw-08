import sys

from book.address_book import AddressBook
from book.record import Record
from bot.decorators import input_error
from storage import save_data


@input_error
def close_command(book: AddressBook):
    save_data(book)
    print('Good bye!')
    sys.exit(1)


@input_error
def hello_command():
    print('How can I help you?')


@input_error
def add_contact_command(args: list, book: AddressBook):
    if len(args) != 2:
        raise ValueError('Invalid number of arguments. Example: add John 1111111111')

    name, phone = args

    record = book.find(name)
    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        print('Contact added.')
    else:
        record.add_phone(phone)
        print('Phone added to existing contact.')


@input_error
def change_contact_command(args: list, book: AddressBook):
    if len(args) != 3:
        raise ValueError('Invalid number of arguments. Example: change John 1111111111 2222222222')

    name, phone, new_phone = args

    record = book.find(name)
    if record is None:
        raise ValueError('Contact not found.')
    else:
        record.edit_phone(phone, new_phone)
        print('Phone changed.')


@input_error
def get_contact_command(args: list, book: AddressBook):
    if len(args) != 1:
        raise ValueError('Invalid number of arguments. Example: phone John')

    [name] = args

    record = book.find(name)
    if record is None:
        print('Contact not found.')
    else:
        print(f"Phones: {', '.join(p.value for p in record.phones)}")


@input_error
def get_contacts_command(book: AddressBook):
    for _, record in book.items():
        print(record)


@input_error
def add_birthday_command(args: list, book: AddressBook):
    if len(args) != 2:
        raise ValueError('Invalid number of arguments. Example: add-birthday John 23.01.1985')

    name, birthday = args

    record = book.find(name)
    if record is None:
        raise ValueError('Contact not found.')
    else:
        record.add_birthday(birthday)
        print('Birthday added.')


@input_error
def show_birthday_command(args: list, book: AddressBook):
    if len(args) != 1:
        raise ValueError('Invalid number of arguments. Example: show-birthday John')

    [name] = args

    record = book.find(name)
    if record is None:
        raise ValueError('Contact not found.')
    else:
        if record.birthday is not None:
            print(f'Birthday: {record.birthday}')
        else:
            raise ValueError('Birthday not set.')


@input_error
def show_birthdays_command(book: AddressBook):
    items = book.get_upcoming_birthdays()

    if not items:
        raise ValueError('No upcoming birthdays.')
    else:
        for item in items:
            print(f"{item['name']}: {item['birthday']}")
