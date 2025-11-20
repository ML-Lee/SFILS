# Scripts – Database Setup for SFILS Assignment 1

This folder contains the SQL scripts used to create and manage the MySQL database required for Assignment 1 of the SFILS project.

Each script is designed to help recreate the database structure and populate data so that results are reproducible on any system.

---

## Files Included

### 1. `create_sfpl_table.sql`
Creates the table:

sfpl_datasf_library_usage_jan_2023


This table stores the SF Public Library usage dataset.  
The script was generated using:



mysqldump --no-data


so it contains only the **schema** (table definition), not the data.

---

### 2. `create_tables.sql`
Template script from the original SFILS repository.  
Creates additional example tables provided by the instructor.  
This file is not directly part of Assignment 1 but remains included for completeness.

---

### 3. `populate_data.sql`
Template script from the original project.  
Populates the example tables created in `create_tables.sql`.

This script does **not** load the SFPL dataset.  
(Assignment 1 uses the table created by `create_sfpl_table.sql`.)

---

### 4. `load_sfpl_data.sql` (optional if you add it later)
Loads the SFPL dataset from a CSV file into the table:



sfpl_datasf_library_usage_jan_2023


Using a command such as:



mysql -u <root> -p --local-infile=1 sfils_db < scripts/load_sfpl_data.sql


---

## How to Use These Scripts

1. Create or select the database:
```sql
CREATE DATABASE sfils_db;
USE sfils_db;


Create the SFPL table:

mysql -u <root> -p sfils_db < scripts/create_sfpl_table.sql


(Optional) Load data:

mysql -u <root> -p --local-infile=1 sfils_db < scripts/load_sfpl_data.sql


Verify:

SHOW TABLES;
DESCRIBE sfpl_datasf_library_usage_jan_2023;


