import pickle

from book.address_book import AddressBook


def save_data(book):
    with open('addressbook.pkl', 'wb') as file:
        pickle.dump(book, file)


def load_data() -> AddressBook:
    try:
        with open('addressbook.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()
