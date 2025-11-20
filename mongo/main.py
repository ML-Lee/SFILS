import mysql.connector
import sys

# ------------------------------
# Database connection
# ------------------------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="sfils_user",       # update if needed
        password="sfils_pass",   # update if needed
        database="sfils_db"
    )

# ------------------------------
# Import functional modules
# ------------------------------
from add_user import add_user
from add_book import add_book
from borrow_book import borrow_book
from list_books import list_books
from search_books import search_books


# ------------------------------
# Menu
# ------------------------------
def main_menu():
    while True:
        print("\n========== SFILS Library System ==========")
        print("1. Add User")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. List Books")
        print("5. Search Books")
        print("6. Exit")
        print("------------------------------------------")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_user()
        elif choice == "2":
            add_book()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            list_books()
        elif choice == "5":
            search_books()
        elif choice == "6":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select 1-6.")

# ------------------------------
# Start Application
# ------------------------------
if __name__ == "__main__":
    try:
        # Quick DB check to ensure connection works
        conn = get_connection()
        print("Connected to MySQL successfully.")
        conn.close()
    except Exception as e:
        print("Database connection failed:", e)
        sys.exit(1)

    main_menu()
