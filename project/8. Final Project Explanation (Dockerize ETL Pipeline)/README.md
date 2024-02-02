**Introduction**
This final project is about Dockerize ETL Pipeline using ETL tools Airflow that extract
Public API data from PIKOBAR, then load into MySQL (Staging Area) and finally
aggregate the data and save into PostgreSQL.

**Project Steps**
1. Create Docker (MySQL, Airflow and PostgreSQL) in your local computer
2. Create Database in MySQL and PostgreSQL
3. Create Connection from Airflow to MySQL and PostgreSQL
4. Create DAG
5. Create DDL in MySQL
6. Get data from Public API covid19 and load data to MySQL
7. Create DDL in PostgreSQL for Fact table and Dimension table
8. Create aggregate Province Daily save to Province Daily Table
9. Create aggregate Province Monthly save to Province Monthly Table
10.Create aggregate Province Yearly save to Province Yearly
11.Create aggregate District Monthly save to District Monthly
12.Create aggregate District Yearly save to District Yearly
13.Schedule the DAG daily save to Province Monthly 
