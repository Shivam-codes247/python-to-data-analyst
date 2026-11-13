-- 1. Create a table feedback(feedback_id INT NOT NULL, comment VARCHAR(200)).
temp=# create table feedback(feedback_id INT NOT NULL , comment varchar(200));

-- 2. Create a table newsletter_signup(email VARCHAR(100) UNIQUE).
temp=# create table newsletter(email varchar(30) UNIQUE);

-- 3. Create a table discount_codes(code VARCHAR(10) PRIMARY KEY, percent_off INT).
temp=# create table discount_code(code varchar(20) PRIMARY KEY , percent_off INT);

-- 4. Create a table orders_log(log_id INT PRIMARY KEY, orderNumber INT NOT NULL, note VARCHAR(100) 
-- DEFAULT 'No note').
temp=# CREATE TABLE ORDERS_LOG(order_id INT PRIMARY KEY,order_no INT NOT NULL , note VARCHAR(100) DEFAULT 'NO NOTE');

-- 5. Create a table promo(id INT PRIMARY KEY, discount INT DEFAULT 10), and explain, without inserting anything yet, 
-- what value discount should end up with if a future row leaves it out.
temp=# CREATE TABLE PROMO(id INT PRIMARY KEY , discount INT DEFAULT 10);

-- 6. Using DESCRIBE, identify which column in jobs (hr) is the primary key.

temp=# \c hr_data
You are now connected to database "hr_data" as user "postgres".
hr_data=# \d jobs
                                       Table "public.jobs"
   Column   |         Type          | Collation | Nullable |               Default
------------+-----------------------+-----------+----------+--------------------------------------
 job_id     | integer               |           | not null | nextval('jobs_job_id_seq'::regclass)
 job_title  | character varying(35) |           | not null |
 min_salary | numeric(8,2)          |           |          | NULL::numeric
 max_salary | numeric(8,2)          |           |          | NULL::numeric
Indexes:
    "jobs_pkey" PRIMARY KEY, btree (job_id)   
    -- so we can see job_id is a primary key
   
-- 7. Using DESCRIBE, identify which columns look like they together form the composite primary key of 
-- orderdetails (cm) (hint: check the Key column in the output).
temp=# \c customer_db
You are now connected to database "customer_db" as user "postgres".


customer_db=# \d orderdetails
                       Table "public.orderdetails"
     Column      |         Type          | Collation | Nullable | Default
-----------------+-----------------------+-----------+----------+---------
 orderNumber     | integer               |           | not null |
 productCode     | character varying(15) |           | not null |
 quantityOrdered | integer               |           | not null |
 priceEach       | numeric(10,2)         |           | not null |
 orderLineNumber | smallint              |           | not null |
Indexes:
    "orderdetails_pkey" PRIMARY KEY, btree ("orderNumber", "productCode")
    "orderdetails_productCode_idx" btree ("productCode")
Foreign-key constraints:
    "orderdetails_ibfk_1" FOREIGN KEY ("orderNumber") REFERENCES orders("orderNumber")
    "orderdetails_ibfk_2" FOREIGN KEY ("productCode") REFERENCES products("productCode")

    The composite primary key of the orderdetails table is formed by orderNumber and productCode. 
    Neither column alone is necessarily unique, but their combination uniquely identifies each record.

-- 8. Create a table signup_form(user_id INT PRIMARY KEY, email VARCHAR(100) UNIQUE, 
-- joined_on DATE NOT NULL, plan VARCHAR(20) DEFAULT 'free'), combining all four constraints 
-- from this topic in one table.

customer_db=# \d signup_form
                              Table "public.signup_form"
  Column   |         Type          | Collation | Nullable |          Default
-----------+-----------------------+-----------+----------+---------------------------
 user_id   | integer               |           | not null |
 email     | character varying(30) |           |          |
 joined_on | date                  |           | not null |
 plan      | character varying(15) |           |          | 'FREE'::character varying
Indexes:
    "signup_form_pkey" PRIMARY KEY, btree (user_id)
    "signup_form_email_key" UNIQUE CONSTRAINT, btree (email)

-- 9. Create a table inventory_check(check_id INT PRIMARY KEY, productCode VARCHAR(15) NOT NULL, 
-- status VARCHAR(20) DEFAULT 'pending').

customer_db=# \d inventory_check
                               Table "public.inventory_check"
    Column    |         Type          | Collation | Nullable |           Default
--------------+-----------------------+-----------+----------+------------------------------
 check_id     | integer               |           | not null |
 product_code | character varying(15) |           | not null |
 status       | character varying     |           |          | 'pending'::character varying
Indexes:
    "inventory_check_pkey" PRIMARY KEY, btree (check_id)

-- 10. In your own words, explain the difference between PRIMARY KEY and UNIQUE, both block duplicates, 
-- so what's actually different?
|               PRIMARY KEY                     |               UNIQUE                                      |

| Uniquely identifies each row in a table.      |  Ensures that values in a column (or combination of columns) 
                                                   are not duplicated. 
| Does not allow NULL values.                   | Allows NULL values in PostgreSQL. 
| Only one PRIMARY KEY is allowed per table.    | Multiple UNIQUE constraints can exist in a table. 