import inspect

from bot.commands import close_command, hello_command, add_contact_command, change_contact_command, \
    get_contact_command, get_contacts_command, add_birthday_command, show_birthday_command, show_birthdays_command
from storage import load_data


def parse_input(user_input: str) -> tuple:
    command, *args = user_input.lower().split()
    return command, args


commands = {
    'close': close_command,
    'exit': close_command,
    'hello': hello_command,
    'add': add_contact_command,
    'change': change_contact_command,
    'phone': get_contact_command,
    'all': get_contacts_command,
    'add-birthday': add_birthday_command,
    'show-birthday': show_birthday_command,
    'birthdays': show_birthdays_command
}


def start():
    book = load_data()
    print('Welcome to the assistant bot!')

    while True:
        user_input = input('Enter a command: ')
        try:
            command, args = parse_input(user_input)
        except ValueError:
            print('Input is empty.')
            continue

        if command in commands:
            unwrapped_function = inspect.unwrap(commands[command])
            sig = inspect.signature(unwrapped_function)
            if len(sig.parameters) == 0:
                commands[command]()
            elif len(sig.parameters) == 1:
                commands[command](book)
            elif len(sig.parameters) == 2:
                commands[command](args, book)
        else:
            print('Invalid command.')
