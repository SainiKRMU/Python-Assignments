# Library Inventory Manager

A **modular, object-oriented Python project** for managing books in a library. The system supports adding books, issuing and returning them, searching the catalog, and maintaining persistent data storage using JSON.

---

## Project Overview

This project demonstrates:

- **Object-Oriented Programming (OOP)**
- **JSON file handling** for data persistence
- **Exception handling and logging**
- **Modular package structure**
- **Menu-driven command-line interface (CLI)**

The program automatically loads and updates a JSON catalog, allowing repeated use without data loss.

---

## Folder Structure

LIBRARY_INVENTORY_MANAGER/
|
├── cli/
|   └── main.py
|
├── library_manager/
|   ├── __init__.py
|   ├── book.py
|   └── inventory.py
|
├── data/
|   └── books.json
|
├── logs/
|   └── app.log
|
├── README.txt
└── report.txt

------------------------------------------------------------

## HOW TO RUN

1. Open terminal inside the project folder:

   LIBRARY_INVENTORY_MANAGER/

2. Run the main program:

   python cli/main.py

   If module errors appear in VS Code, try:

   python -m cli.main

------------------------------------------------------------

## CORE FEATURES

- Add new books (title, author, ISBN)
- Issue and return books
- Search by title or ISBN
- View full inventory
- Automatic JSON saving and loading
- Logging of all actions (INFO and ERROR)

------------------------------------------------------------

## CLASSES

**Book**
- Stores book details and status.
- Methods: issue(), return_book(), is_available(), to_dict()

**LibraryInventory**
- Handles all inventory operations.
- Methods: add_book(), issue_book(), return_book(), search_by_title(), search_by_isbn(), display_all(), save_to_file(), load_from_file()

------------------------------------------------------------

## PERSISTENCE

All book data is stored in:

   **data/books.json**

The file is created automatically if missing.

------------------------------------------------------------

## LOGGING

All events are logged to:

  **logs/app.log**

Logs include:
- Book additions
- Issues and returns
- Errors (duplicate ISBN, not found, invalid operations)

------------------------------------------------------------

## Author

**Disha Saini**

B.Tech CSE (AI&ML)

Section : A
