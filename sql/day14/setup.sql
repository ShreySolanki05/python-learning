DROP TABLE IF EXISTS employees;
CREATE TABLE employees(
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL, 
    city TEXT,
    salary NUMERIC(10,2) NOT NULL,
    hire_date DATE NOT NULL
);

INSERT INTO employees(name,department,city,salary,hire_date)
VALUES('Asha Verma','Engineering','Bengaluru',85000,'2021-06-14'),
      ('Ravi Kulkarni','Engineering','Pune',72000,'2022-01-10'),
      ('Meera Nair','Sales','Hyderabad',58000,'2020-09-01'),
      ('Kabir Singh','Sales','Noida',61000,'2019-03-25'),
      ('Tara Iyer','HR','Pune',52000,'2023-02-06'),
      ('Dev Malhotra','Engineering','Noida',95000,'2018-11-19'),
      ('Isha Reddy','Support','Hyderabad',39000,'2023-07-17'),
      ('Rohan Das','Support','Bengaluru',41000,'2022-08-29'),
      ('Nisha Kapoor','HR',NULL,56000,'2021-04-12'),
      ('Arjun Mehta','Engineering','Bengaluru',78000,'2020-12-07'),
      ('Pooja Shah','Sales',NULL,64000,'2022-05-30'),
      ('Sameer Khan','Support','Pune',43000,'2021-10-04');


