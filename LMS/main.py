class Library:
    def __init__(self, books):
        self.books = books

    def display_books(self):
        print("\nAvailable books in the Library are:")
        for book in self.books:
            print(f"- {book}")

    def lend_book(self, book_name, user):
        for book in self.books:
            if book.lower() == book_name.lower():
                print(f"{user} has borrowed '{book}'")
                self.books.remove(book)
                return
        print(f"Sorry, '{book_name}' is not available at the moment.")

    def return_book(self, book_name):
        for book in self.books:
            if book.lower() == book_name.lower():
                print(f"'{book_name}' is already in the library.")
                return
        print(f"'{book_name}' has been returned to the library.")
        # Capitalize properly (optional) or keep original casing
        self.books.append(book_name.title())

# Main Program
lib = Library([
    "Python Basics", "Machine Learning", "Data Structures", 
    "AI for Beginners", "Atomic Habits", 
    "Dopamine Detox", "Data Analysis with Python"
])

while True:
    print("\n Welcome to the Library!")
    print("1. Display Available Books")
    print("2. Lend a book")
    print("3. Return a book")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 4.")
        continue

    if choice == 1:
        lib.display_books()
    elif choice == 2:
        book_name = input("Enter the name of the book you want to borrow: ")
        user = input("Enter your name: ")
        lib.lend_book(book_name, user)
    elif choice == 3:
        book_name = input("Enter the name of the book you want to return: ")
        lib.return_book(book_name)
    elif choice == 4:
        print("Thank you for using the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
