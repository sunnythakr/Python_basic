class Book:
    def __init__(self, title, author, isbn):
        self._title = title  # Encapsulated attribute
        self._author = author  # Encapsulated attribute
        self._isbn = isbn  # Encapsulated attribute
        self._is_available = True  # Encapsulated attribute for availability

    def borrow(self):
        if self._is_available:
            self._is_available = False
            print(f"Book '{self._title}' by {self._author} is borrowed.")
        else:
            print(f"Sorry, '{self._title}' is currently unavailable.")

    def return_book(self):
        if not self._is_available:
            self._is_available = True
            print(f"Book '{self._title}' by {self._author} is returned. Thank you!")
        else:
            print(f"'{self._title}' is already available.")

    def display_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"ISBN: {self._isbn}")
        availability = "Available" if self._is_available else "Not Available"
        print(f"Availability: {availability}")


class Patron:
    def __init__(self, name, library_card_number):
        self._name = name  # Encapsulated attribute
        self._library_card_number = library_card_number  # Encapsulated attribute
        self._books_borrowed = []  # Encapsulated attribute for borrowed books

    def borrow_book(self, book):
        if len(self._books_borrowed) < 3:
            self._books_borrowed.append(book)
            book.borrow()
            print(f"{self._name} borrowed '{book._title}'")
        else:
            print(f"{self._name} has reached the maximum borrowing limit.")

    def return_book(self, book):
        if book in self._books_borrowed:
            self._books_borrowed.remove(book)
            book.return_book()
            print(f"{self._name} returned '{book._title}'")
        else:
            print(f"{self._name} did not borrow '{book._title}'")

    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Library Card Number: {self._library_card_number}")
        borrowed_books = ", ".join([book._title for book in self._books_borrowed])
        print(f"Borrowed Books: {borrowed_books}")


class Library:
    def __init__(self):
        self._books = []  # Encapsulated attribute for library books
        self._patrons = []  # Encapsulated attribute for library patrons

    def add_book(self, book):
        self._books.append(book)
        print(f"Added '{book._title}' to the library")

    def add_patron(self, patron):
        self._patrons.append(patron)
        print(f"Added '{patron._name}' as a patron")

    def display_books(self):
        print("Library Books:")
        for book in self._books:
            book.display_info()

    def display_patrons(self):
        print("Library Patrons:")
        for patron in self._patrons:
            patron.display_info()


# Creating instances of the Book, Patron, and Library classes
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

patron1 = Patron("Alice Johnson", "L123")
patron2 = Patron("Bob Smith", "M456")

library = Library()

# Using encapsulated methods to interact with the objects
library.add_book(book1)
library.add_book(book2)

library.add_patron(patron1)
library.add_patron(patron2)

library.display_books()
library.display_patrons()

patron1.borrow_book(book1)
patron1.borrow_book(book2)
patron1.borrow_book(book2)  # Trying to borrow too many books

patron2.borrow_book(book2)
patron2.return_book(book1)
patron2.return_book(book1)  # Trying to return a book not borrowed

library.display_books()
library.display_patrons()