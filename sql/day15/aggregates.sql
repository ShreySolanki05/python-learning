select count(*) from employees;

select count(city) from employees; -- its different than task 1 as it only gives the count of employees
-- who have something inside their city column and will leave any null city value

select sum(salary) as total_salary from employees;

select round(avg(salary), 2) as avg_salary from employees;

select max(salary) as maximum_salary , min(salary) as minimum_salary from employees;

select count(department) as engineers , round(avg(salary), 2) as avg_salary from employees where department = 'Engineering';

select count(distinct city) from employees;

select name, max(salary) from employees; -- this doesnt work as it is trying to print a whole name column 
-- with a single aggregate functions result 
select name , salary from employees order by salary desc limit 1;

