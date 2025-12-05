#Mini Project Assignment: Library Inventory Manager

#------------------------------------------------------------------------------------------------------

# Course            : Programming for Problem Solving using Python
# Assignment Title  : Object-Oriented Design and Robust Programming in a Library Management System
# Name              : Disha Saini
# Roll no.          : 2501730318
# Computer Science Engineering (AI & ML)
# Section           : A

#____________________________________________________________________________________________________

# main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def menu():
    print("\n=== LIBRARY INVENTORY MANAGER ===")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")
    return input("Choose an option: ")

def main():
    inventory = LibraryInventory()

    while True:
        choice = menu()

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            inventory.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_books()
                print("Book issued.")
            else:
                print("Book not available.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.return_book():
                inventory.save_books()
                print("Book returned.")
            else:
                print("Book not found or not issued.")

        elif choice == "4":
            books = inventory.display_all()
            print("\n--- ALL BOOKS ---")
            for b in books:
                print(b)

        elif choice == "5":
            title = input("Enter title to search: ")
            results = inventory.search_by_title(title)
            for b in results:
                print(b)
            if not results:
                print("No books found.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

