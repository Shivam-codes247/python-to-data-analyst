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
   
-- 7. Using DESCRIBE, identify which columns look like they together form the composite primary key of orderdetails (cm) (hint: check the Key column in the output).
-- 8. Create a table signup_form(user_id INT PRIMARY KEY, email VARCHAR(100) UNIQUE, joined_on DATE NOT NULL, plan VARCHAR(20) DEFAULT 'free'), combining all four constraints from this topic in one table.
-- 9. Create a table inventory_check(check_id INT PRIMARY KEY, productCode VARCHAR(15) NOT NULL, status VARCHAR(20) DEFAULT 'pending').
-- 10. In your own words, explain the difference between PRIMARY KEY and UNIQUE, both block duplicates, so what's actually different?