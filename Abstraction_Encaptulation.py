# Abstraction and Encaptulation
# Layers of Abstraction such as lend a book, return a book

class Library:

    def __init__(self, availableBooks):
        self.availableBooks = listOfBooks

    def displAyavailableBooks():
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("Here is your book")
            self.availableBooks.remove(requestedBook)
        else:
            print("sorry this book does not exist")

    def addBook(self, addedBook):
        if addedBook not in self.availableBooks:
            self.availableBooks.append(addedBook)
            print("The book has been returned")

class Customer:
    def requestABook(self):
        print("Enter the name of the book you would like to borrow:")
        self.book = input()
        return self.book

    def returnABook(self):
        print("Thank you. The book is back to the library")
        self.book = input()
        return self.book

while True:
    print("Enter 1 to ask for the book availability")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit the program")
    library = Library (["Pride and Pejudice", "Great Expectations", "Once upon a time"])
    customer = Customer()
    userChoice = str(input())
    if userChoice is 1:
        library.displAyavailableBooks()
    elif userChoice is 2:
        customer.requestABook()
        library.lendBook()
    elif userChoice is 3:
        library.addBook()
        customer.returnABook
    else:
        quit()
