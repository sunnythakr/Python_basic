



class Book:
    def __init__(self, title, author, genre):
        self._title = title  # Encapsulated attribute
        self._author = author 
        self._genre = genre  
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

    def display_book_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Genre: {self._genre}")
        availability = "Available" if self._is_available else "Not Available"
        print(f"Availability: {availability}")


# Creating instances of the Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
book2 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy")

# Using encapsulated methods to interact with the objects
book1.display_book_info()
book1.borrow()
book1.display_book_info()
book1.return_book()
book1.display_book_info()

book2.display_book_info()
book2.borrow()
book2.borrow()
book2.display_book_info()
book2.return_book()
book2.display_book_info()
