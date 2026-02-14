class Book:
    '''
        Represents a single book in library 
    '''

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True # By Default book is available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} | ISBN : {self.isbn} | {status}" 
    
    def mark_borrowed(self):
        self.available = False
    
    def mark_returned(self):
        self.available = True


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
    
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book

        return None

    def borrow_book(self, isbn):
        book = self.find_book(isbn)

        if book and book.available:
            book.mark_borrowed()
            print("Book borrowed successfully...")
        else:
            print("Book not found or already borrowed.")

    def return_book(self, isbn):
        book = self.find_book(isbn)

        if book and not book.available:
            book.mark_returned()
            print("Book returned successfully...")
        else:
            print("Invalid return request.")

    def display_available_books(self):
        available_books = [book for book in self.books if book.available]

        if not available_books:
            print("No Books Available...")
        else:
            for book in available_books:
                print(book)

    def display_all_books(self):
        for book in self.books:
            print(book)

if __name__ == "__main__":
    library = Library()

    print("\n-------------------------------------------------------------\n")

    print("Adding Books")
    print("Book 1:", "['Python Basics', 'John Doe', 101]")
    print("Book 2:", "['AI Fundamentals', 'Jane Smith', 102]")

    book1 = Book("Python Basics", "John Doe", "101")
    book2 = Book("AI Fundamentals", "Jane Smith", "102")

    library.add_book(book1)
    library.add_book(book2)

    print("Added Books in Library")

    print("\n-------------------------------------------------------------\n")

    print("Books Available in Library")

    library.display_available_books()

    print("\n-------------------------------------------------------------\n")

    print("Borrowing Books: ISBN - 101")
    library.borrow_book("101")
    library.display_available_books()

    print("\n-------------------------------------------------------------\n")

    print("Show all books after bowrrowing one")
    library.display_all_books()

    print("\n-------------------------------------------------------------\n")

    library.return_book("101")
    library.display_available_books()

    
    print("\n-------------------------------------------------------------\n")

    print("Show all books after recieving one")
    library.display_all_books()
    
    print("\n-------------------------------------------------------------\n")
