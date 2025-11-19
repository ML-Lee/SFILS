\# SFILS Assignment 1 – Database Setup



This project uses MySQL as the database system.



\## Prerequisites



\- MySQL installed and running

\- A MySQL user account with permissions to create databases and tables (for example, `root`)



\## Recreating the SFPL table



The `scripts/create\_sfpl\_table.sql` file was generated from my local `sfils\_db` database

using `mysqldump` with the `--no-data` option. It contains the `CREATE TABLE` statement

for the `sfpl\_datasf\_library\_usage\_jan\_2023` table.



To create the table in a database (for example, `sfils\_db`):



```bash

mysql -u <root> -p sfils\_db < scripts/create\_sfpl\_table.sql







