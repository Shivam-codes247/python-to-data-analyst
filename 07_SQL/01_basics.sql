-- SQL BASICS: DATABASES, TABLES, AND DATA TYPES
-- ============================================================

-- 1. Create a practice database.
-- Run once. PostgreSQL reports an error if retail_lab already exists.
CREATE DATABASE retail_lab;


-- 2. Connect to the existing Classic Models practice database.
-- Change "cm" here if your database has a different name.
\c cm


-- 3. List databases available to the current PostgreSQL server.
\l


-- 4. Inspect the employees table from the HR practice dataset.
-- The hr database must contain the imported HR tables.
\c hr
\d employees


-- 5. Create a stock table in the Classic Models database.
-- Each column is named and typed for its stored value.
\c cm
CREATE TABLE warehouse_stock (
    stock_id INT,
    product_code VARCHAR(15),
    quantity INT,
    last_checked DATE
);


-- 6. Import the Classic Models dataset into customer_db and list its tables.
-- \ir resolves this path relative to this script's location.
-- The dump contains DROP TABLE statements, so use a disposable database.
\c customer_db
\ir ../01_practice_data/cm_postgres.sql
\dt
-- Expected: 8 tables.


-- 7. Create a catalog table.
-- DATE stores a calendar date without a time of day.
CREATE TABLE product_catalog (
    catalog_id INT,
    product_code VARCHAR(15),
    added_on DATE
);


-- 8. Create a staff directory table.
-- Use VARCHAR for names and department codes; DATE for the hire date.
CREATE TABLE staff_directory (
    staff_id INT,
    full_name VARCHAR(80),
    hire_date DATE,
    dept_code VARCHAR(10)
);


-- 9. Match the offices.officeCode data type and exact identifier case.
-- The imported offices column is VARCHAR(10), quoted as "officeCode".
-- Keeping the same type and case allows a compatible foreign key later.
CREATE TABLE office_notes (
    "officeCode" VARCHAR(10)
);


-- 10. Inspect product column types and constraints.
\d products

-- Notes from the products table:
--   * productCode is VARCHAR(15) and is the primary key.
--   * Name, line, scale, and vendor columns use VARCHAR.
--   * productDescription uses TEXT for longer descriptions.
--   * quantityInStock uses SMALLINT for a small whole-number quantity.
--   * buyPrice and MSRP use NUMERIC(10,2) for exact two-decimal values.
--   * In PostgreSQL, DECIMAL and NUMERIC are equivalent types;
--     VARCHAR and CHARACTER VARYING are also equivalent.
