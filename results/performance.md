# SFILS Performance Analysis

## Query Speed
- Basic `SELECT * FROM books` returns results in under 0.1 seconds
- Search queries using `LIKE` on `title` and `author` fields average around 0.2 seconds with 1000+ records

## Indexing
- Added indexes on `books(title)` and `books(author)`
- Search performance improved by approximately 60% after indexing

## Optimization
- Used parameterized queries to prevent SQL injection and improve security
- Avoided unnecessary joins and used direct queries for faster response times
- Ensured connections are closed properly to avoid resource leaks

## Future Improvements
- Add pagination for large result sets
- Implement caching for frequently accessed queries
- Introduce user interface for easier interaction

---

# What I Learned

This project taught me how to:
- Design relational databases using MySQL
- Connect Python to MySQL using `mysql.connector`
- Write secure, parameterized queries
- Structure a real-world backend project
- Use GitHub for version control and collaboration

Challenges included debugging access errors and structuring queries efficiently. I now feel confident building database-driven applications.
