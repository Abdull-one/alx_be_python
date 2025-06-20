class Book:
    """
    Represents a book in the library.
    """

    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """
        Marks the book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Marks the book as returned.
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Checks if the book is available (not checked out).

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the book.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of books.
    """

    def __init__(self):
        """
        Initializes a new Library instance.
        """
        self._books = []  # Private list to store books

    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
            book (Book): The Book object to add.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book from the library by title.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' not found or already checked out.")

    def return_book(self, title):
        """
        Returns a book to the library by title.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' not found or already returned.")

    def list_available_books(self):
        """
        Lists all available books in the library.
        """
        for book in self._books:
            if book.is_available():
                print(book)