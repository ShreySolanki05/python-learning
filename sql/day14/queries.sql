SELECT * FROM employees; --1
SELECT name , salary FROM employees; --2
SELECT * FROM employees WHERE department = 'Engineering'; --3
SELECT * FROM employees WHERE salary > 60000; --4
SELECT * FROM employees WHERE department = 'Engineering' AND salary >= 80000; --5
SELECT * FROM employees WHERE city = 'Pune' OR city = 'Noida'; --6a
SELECT * FROM employees WHERE city IN ('Pune','Noida'); --6b
SELECT * FROM employees WHERE hire_date BETWEEN '2021-01-01' AND '2022-12-31'; --7
SELECT * FROM employees WHERE name LIKE 'A%'; --8
SELECT * FROM employees WHERE city IS NULL; --9
SELECT * FROM employees ORDER BY salary DESC LIMIT 3; --10
SELECT DISTINCT department FROM employees; --11a
SELECT DISTINCT city FROM employees; --11b
SELECT * FROM employees ORDER BY department ASC , salary DESC; --12