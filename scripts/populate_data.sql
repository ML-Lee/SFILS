INSERT INTO users (name, email, card_number) VALUES
('Alice Smith', 'alice@example.com', 'SF12345'),
('Bob Jones', 'bob@example.com', 'SF67890');

INSERT INTO books (title, author, genre, isbn, available) VALUES
('1984', 'George Orwell', 'Dystopian', '9780451524935', TRUE),
('To Kill a Mockingbird', 'Harper Lee', 'Classic', '9780061120084', TRUE);

INSERT INTO borrow_records (user_id, book_id, borrow_date, return_date) VALUES
(1, 1, '2025-10-01', NULL);
