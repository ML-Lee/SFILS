# SFILS Assignment 1 – Database Setup & Documentation

This project is part of the San Francisco Integrated Library System (SFILS) assignment.  
The goal of this phase is to properly create, structure, and reproduce the MySQL database used by the project.

This README provides clear instructions on how to recreate the database, run the SQL scripts, and verify that the table structure matches the dataset requirements.

---

## Project Documentation

The `docs/` folder contains:
- Instructions on how to set up the database
- Notes and technical details needed for reproducibility
- Screenshots or supplementary files (if needed later)

---

## Database System

This project uses MySQL as the database system (MariaDB is also acceptable).

The main table used in this project is:

sfpl_datasf_library_usage_jan_2023

It is created using the SQL script located in:

scripts/create_sfpl_table.sql

This script contains only the schema and was generated using:

mysqldump --no-data


## Recreating the SFPL Table

Follow the steps below to recreate the database structure.

### 1. Ensure MySQL is installed and running
You must have a MySQL user with privileges, such as:
- root
- or another configured user

### 2. Create or select the database

```sql
CREATE DATABASE sfils_db;
USE sfils_db;


3. Run the script to create the table
From the project folder:

mysql -u <user> -p sfils_db < scripts/create_sfpl_table.sql

Replace <user> with your MySQL username. For example, mine is root, so:

mysql -u root -p sfils_db < scripts/create_sfpl_table.sql


Verifying the Setup
After running the script, open the MySQL client:

mysql -u <user> -p

Inside MySQL:

USE sfils_db;
SHOW TABLES;

You should see:

sfpl_datasf_library_usage_jan_2023

To inspect the table structure:

DESCRIBE sfpl_datasf_library_usage_jan_2023;

To confirm the table exists and responds:

SELECT * FROM sfpl_datasf_library_usage_jan_2023 LIMIT 10;


Summary
This README documents how to:

Recreate the MySQL database

Run the provided SQL schema script

Verify table structure and functionality

Understand the purpose of the docs/ directory

This satisfies the Assignment 1 rubric requirements for documentation, database reproducibility, and project clarity
