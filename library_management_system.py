class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_available = True

    def get_title(self):
        return self.__title
    
    def is_available(self):
        return self.__is_available
    
    def borrow_book(self):
        if self.__is_available = True:
            self.__is_available = False
            return True
        return False
    
    def return_book(self):
        self.__is_available = True

def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    library[isbn] = Book(title, author, isbn)

def checkout_book(library, current_loans):
    isbn = input("Enter ISBN of the book to borrow: ")
    user = input("Enter user name: ")
    if isbn in library and library[isbn].borrow_book():
        current_loans[isbn] = user
        print(f"Book '{library[isbn].get_title()}' checked out to {user}.")
    else:
        print("Book not available or not found.")

def checkin_book(library, current_loans):
    isbn = input("Enter ISBN of the book to return: ")
    if isbn in library and isbn in current_loans:
        library[isbn].return_book()
        del current_loans[isbn]
        print(f"Book '{library[isbn].get_title()}' returned.")
    else:
        print("Invalid ISBN or the book was not found.")

def main():
    library = {}
    current_loans = {}
    while True:
        print("\n1. Add Book\n2. Checkout Book\n3. Checkin Book\n4. Exit")
        choice = input("Enter your choice: ").lower()
        try:
            if choice == "1":
                add_book(library)
            elif choice == "2":
                checkout_book(library, current_loans)
            elif choice == "3":
                checkin_book(library, current_loans)
            elif choice == "4":
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()