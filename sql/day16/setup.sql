DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    location VARCHAR(50)
);

CREATE TABLE staff (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    dept_id INT REFERENCES departments(id),
    salary NUMERIC(10,2)
);

INSERT INTO departments (name, location) VALUES
('Engineering', 'Bengaluru'),
('Sales', 'Mumbai'),
('HR', 'Delhi'),
('Support', 'Noida'),
('Legal', 'Pune');

INSERT INTO staff (name, dept_id, salary) VALUES
('Aarav', 1, 90000),
('Meera', 1, 75000),
('Rohan', 1, 82000),
('Isha', 2, 60000),
('Kabir', 2, 58000),
('Neha', 3, 52000),
('Vikram', 4, 41000),
('Sana', 4, 43000),
('Dev', NULL, 50000),
('Tara', 2, 65000);