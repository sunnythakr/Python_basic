# a LibraryManagementSystem in Python. This system simulates a library 
# with books, members, borrowing, and returns. It showcases encapsulation,
#  interactions, and system management
class Book:
    def __init__(self, book_id, title, author, total_copies):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._total_copies = total_copies
        self._available_copies = total_copies
        self._borrowers = []

    def borrow_book(self, member):
        if self._available_copies > 0:
            borrowing = Borrowing(self, member)
            self._borrowers.append(member)
            self._available_copies -= 1
            member.borrow_book(borrowing)
            print(f"{member._name} borrowed '{self._title}'")
        else:
            print(f"'{self._title}' is currently unavailable")

    def return_book(self, member):
        if member in self._borrowers:
            borrowing = member.return_book(self)
            self._borrowers.remove(member)
            self._available_copies += 1
            print(f"{member._name} returned '{self._title}'")
        else:
            print(f"{member._name} did not borrow '{self._title}'")

    def display_info(self):
        print(f"Book ID: {self._book_id}")
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Available Copies: {self._available_copies}")

    def display_borrowers(self):
        print("Borrowers:")
        for member in self._borrowers:
            print(member._name)


class Member:
    def __init__(self, member_id, name):
        self._member_id = member_id
        self._name = name
        self._borrowings = []

    def borrow_book(self, borrowing):
        self._borrowings.append(borrowing)

    def return_book(self, book):
        for borrowing in self._borrowings:
            if borrowing._book == book:
                self._borrowings.remove(borrowing)
                return borrowing

    def display_info(self):
        print(f"Member ID: {self._member_id}")
        print(f"Name: {self._name}")

    def display_borrowings(self):
        print("Borrowings:")
        for borrowing in self._borrowings:
            print(f"Book: '{borrowing._book._title}' - Due Date: {borrowing._due_date}")


class Borrowing:
    def __init__(self, book, member):
        self._book = book
        self._member = member
        self._due_date = "2023-12-31"


class LibraryManagementSystem:
    def __init__(self):
        self._books = {}
        self._members = {}

    def add_book(self, book):
        self._books[book._book_id] = book
        print(f"Added book '{book._title}' by {book._author}")

    def add_member(self, member):
        self._members[member._member_id] = member
        print(f"Added member {member._name} to the system")

    def display_books(self):
        print("Books:")
        for book in self._books.values():
            print(f"Book ID: {book._book_id} - Title: {book._title}")

    def display_members(self):
        print("Members:")
        for member in self._members.values():
            print(f"Member ID: {member._member_id} - Name: {member._name}")


# Creating instances of the Book, Member, and LibraryManagementSystem classes
library_system = LibraryManagementSystem()

book1 = Book("B001", "The Catcher in the Rye", "J.D. Salinger", 5)
book2 = Book("B002", "To Kill a Mockingbird", "Harper Lee", 7)

library_system.add_book(book1)
library_system.add_book(book2)

member1 = Member("M001", "Alice Johnson")
member2 = Member("M002", "Bob Smith")

library_system.add_member(member1)
library_system.add_member(member2)

book1.borrow_book(member1)
book2.borrow_book(member2)

book1.return_book(member1)
book2.return_book(member2)

book1.borrow_book(member1)
book2.borrow_book(member2)

book1.borrow_book(member2)

book1.display_info()
book1.display_borrowers()

member1.display_info()
member1.display_borrowings()

library_system.display_books()
library_system.display_members()
