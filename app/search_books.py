import mysql.connector

def search_books():
    print("\n--- Search Books ---")
    keyword = input("Enter a keyword to search (title or author): ").strip()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="sfils_user",
            password="sfils_pass",
            database="sfils_db"
        )

        cursor = conn.cursor()
        query = """
            SELECT id, title, author, genre, year
            FROM books
            WHERE title LIKE %s OR author LIKE %s
        """
        cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
        results = cursor.fetchall()

        if not results:
            print("No books found matching that keyword.")
            return

        print("\nID | Title | Author | Genre | Year")
        print("-----------------------------------------")

        for row in results:
            book_id, title, author, genre, year = row
            print(f"{book_id} | {title} | {author} | {genre} | {year}")

    except mysql.connector.Error as err:
        print("Error searching for books:", err)

    finally:
        if conn.is_connected():
            conn.close()
