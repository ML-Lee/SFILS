import os

while True:
    print("\n=== MongoDB Library App ===")
    print("1. Add User")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. List Books")
    print("5. Search Books")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        os.system("python mongo_add_user.py")
    elif choice == "2":
        os.system("python mongo_add_book.py")
    elif choice == "3":
        os.system("python mongo_borrow_book.py")
    elif choice == "4":
        os.system("python mongo_list_books.py")
    elif choice == "5":
        os.system("python mongo_search_books.py")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
