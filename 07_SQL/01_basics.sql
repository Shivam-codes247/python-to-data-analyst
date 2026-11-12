-- SQL BASICS: DATABASES, TABLES, AND DATA TYPES
-- ============================================================
-- Dialect: PostgreSQL, using the psql command-line client.
-- The backslash commands below (\c, \l, \d, \dt, and \ir) are
-- psql commands, not standard SQL and not MySQL commands.
--
-- Run this file from the repository root in PowerShell:
--   psql -d postgres -f "07_SQL/02_basics/practice_questions.sql"
--
-- Prerequisites:
--   * PostgreSQL is running and the current user can create databases.
--   * The cm and hr databases exist before their exercises below.
--   * The customer_db database exists before exercise 6.
--   * To prepare hr, run from the repository root:
--       psql -d hr -f "07_SQL/01_practice_data/hr_postgres.sql"
--
-- Exercises 2 and 5 use the cm database. Exercises 6-10 use
-- customer_db. They are separate examples; change the \c commands if
-- you prefer to do all exercises in one practice database.
--
-- SAFETY: cm_postgres.sql drops and recreates tables with matching
-- names. Import it only into a disposable practice database, never
-- into a production or otherwise valuable database.
--
-- PostgreSQL folds unquoted identifiers to lowercase. The practice
-- tables below use snake_case; the quoted officeCode column in
-- exercise 9 preserves the exact case of the imported offices column.


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
