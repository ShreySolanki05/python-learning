select department, count(*) , round(avg(salary), 2) as avg_salary, max(salary) as top_salary from employees 
group by department order by avg_salary desc;