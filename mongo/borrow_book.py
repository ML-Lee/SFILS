import mysql.connector
from datetime import datetime

def borrow_book():
    print("\n--- Borrow a Book ---")

    user_id = input("Enter user ID: ").strip()
    book_id = input("Enter book ID: ").strip()

    # Basic validation
    if not user_id.isdigit() or not book_id.isdigit():
        print("User ID and Book ID must be numbers.")
        return

    borrow_date = datetime.now().strftime('%Y-%m-%d')

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="sfils_user",
            password="sfils_pass",
            database="sfils_db"
        )
        cursor = conn.cursor()

        # -----------------------------
        # Check if user exists
        # -----------------------------
        cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
        user_exists = cursor.fetchone()

        if not user_exists:
            print(f"❌ User ID {user_id} does not exist.")
            return

        # -----------------------------
        # Check if book exists
        # -----------------------------
        cursor.execute("SELECT id FROM books WHERE id = %s", (book_id,))
        book_exists = cursor.fetchone()

        if not book_exists:
            print(f"❌ Book ID {book_id} does not exist.")
            return

        # -----------------------------
        # Optional: Check if book is already borrowed
        # You can remove this if your assignment does not require it.
        # -----------------------------
        cursor.execute("""
            SELECT * FROM borrow_records
            WHERE book_id = %s AND return_date IS NULL
        """, (book_id,))
        already_borrowed = cursor.fetchone()

        if already_borrowed:
            print(f"❌ Book ID {book_id} is already borrowed.")
            return

        # -----------------------------
        # Insert borrow record
        # -----------------------------
        cursor.execute(
            "INSERT INTO borrow_records (user_id, book_id, borrow_date) VALUES (%s, %s, %s)",
            (user_id, book_id, borrow_date)
        )
        conn.commit()

        print("✅ Borrow record added successfully!")

    except mysql.connector.Error as err:
        print("Error borrowing book:", err)

    finally:
        if conn.is_connected():
            conn.close()
