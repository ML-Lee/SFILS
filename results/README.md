\# Results and Findings – SFILS Assignment 1



This document contains the findings, analysis, queries, and performance notes generated for Assignment 1 using the `sfpl\_datasf\_library\_usage\_jan\_2023` dataset in the MySQL database `sfils\_db`.



The table includes the following columns:



\- Patron Type Code  

\- Patron Type Definition  

\- Total Checkouts  

\- Total Renewals  

\- Age Range  

\- Home Library Code  

\- Home Library Definition  

\- Circulation Active Month  

\- Circulation Active Year  

\- Notification Preference Code  

\- Notification Code Definition  

\- Provided Email Address  

\- Within San Francisco County  

\- Year Patron Registered  



---



\## Queries Used



The following SQL queries were used to explore the dataset.



\### 1. Total number of rows in the dataset

```sql

SELECT COUNT(\*) AS total\_rows

FROM sfpl\_datasf\_library\_usage\_jan\_2023;

2\. Overall total checkouts and renewals

SELECT

&nbsp; SUM(`Total Checkouts`) AS total\_checkouts,

&nbsp; SUM(`Total Renewals`)  AS total\_renewals

FROM sfpl\_datasf\_library\_usage\_jan\_2023;



3\. Top patron types by total checkouts

SELECT

&nbsp; `Patron Type Definition`,

&nbsp; SUM(`Total Checkouts`) AS total\_checkouts

FROM sfpl\_datasf\_library\_usage\_jan\_2023

GROUP BY `Patron Type Definition`

ORDER BY total\_checkouts DESC

LIMIT 5;



4\. Top home libraries by total checkouts

SELECT

&nbsp; `Home Library Definition`,

&nbsp; SUM(`Total Checkouts`) AS total\_checkouts

FROM sfpl\_datasf\_library\_usage\_jan\_2023

GROUP BY `Home Library Definition`

ORDER BY total\_checkouts DESC

LIMIT 5;



5\. Total checkouts by age range

SELECT

&nbsp; `Age Range`,

&nbsp; SUM(`Total Checkouts`) AS total\_checkouts

FROM sfpl\_datasf\_library\_usage\_jan\_2023

GROUP BY `Age Range`

ORDER BY total\_checkouts DESC;



6\. Checkouts inside vs. outside San Francisco County

SELECT

&nbsp; `Within San Francisco County`,

&nbsp; SUM(`Total Checkouts`) AS total\_checkouts,

&nbsp; SUM(`Total Renewals`)  AS total\_renewals

FROM sfpl\_datasf\_library\_usage\_jan\_2023

GROUP BY `Within San Francisco County`;



7\. Total checkouts by circulation year

SELECT

&nbsp; `Circulation Active Year`,

&nbsp; SUM(`Total Checkouts`) AS total\_checkouts

FROM sfpl\_datasf\_library\_usage\_jan\_2023

GROUP BY `Circulation Active Year`

ORDER BY `Circulation Active Year`;



Findings



Based on the executed queries, the dataset contains 437,115 rows of patron

activity. Adult patrons generate the majority of usage, with 34,150,818 total

checkouts, making “Adult” the most active patron type in the system. The home

library with the highest circulation is the Main Library, which accounts for

11,767,324 checkouts, significantly more than any other branch.



In terms of age demographics, patrons aged 10 to 19 years show the highest

engagement, contributing 13,912,059 checkouts. Geographic analysis shows

that the vast majority of library activity comes from San Francisco residents:

66,177,436 checkouts originate from patrons marked as residing within

San Francisco County, compared to 4,235,258 checkouts from non-residents.



Circulation activity increases sharply in recent years. Checkouts jump from

1.6 million in 2019, to 4.6 million in 2020, 6.7 million in 2021,

19.3 million in 2022, and peak at 37.1 million in 2023, indicating

rapidly rising library engagement in the most recent years recorded.



Performance Metrics



For the scale of this dataset, all SQL queries executed quickly (well under one

second) on a local MySQL server. Query performance is efficient due to the

nature of full-table scans on indexed storage engines.



If the dataset were significantly larger, performance could be further improved by:



Adding indexes to frequently grouped or filtered columns

(e.g., Patron Type Definition, Home Library Definition,

Circulation Active Year)



Splitting the dataset into multiple relational tables



Avoiding redundant textual repetition through normalization



Using integer foreign keys instead of large text fields



Database Design Reflection



The SFPL dataset is originally provided as a single large spreadsheet. For

Assignment 1, the dataset was imported into a single MySQL table

(sfpl\_datasf\_library\_usage\_jan\_2023) to simplify initial exploration.



However, for a well-designed relational database, the dataset could be

normalized into multiple tables, such as:



Patron: patron type, age range, registration year



Library: home library codes and definitions



Usage: checkouts, renewals, active year and month



Such a structure would improve scalability, reduce redundancy, and align with

standard database design practices.



The single-table approach was used for simplicity in Assignment 1, but future

project phases could implement a fully normalized schema.



Reproducibility



To reproduce these results:



Create and select the database:



CREATE DATABASE sfils\_db;

USE sfils\_db;





Create the dataset table:



mysql -u <user> -p sfils\_db < scripts/create\_sfpl\_table.sql





Load the CSV dataset into the table using your preferred import method.



Run the SQL queries listed above.



Confirm results match those documented in the Findings section.





