select dept_id , count(*) as headcount from staff where dept_id is not NULL group by dept_id order by headcount desc;

select dept_id , sum(salary) as total_salary from staff group by dept_id having sum(salary) > 150000;

select dept_id , round(avg(salary),2) as avg_sal from staff where salary >= 50000 group by dept_id 
having count(*) > 1;

select dept_id , count(*) from staff where dept_id is not NULL group by dept_id having count(*) < 3;

-- can’t write WHERE COUNT(*) > 2 because aggregate funtions are not alllowed inside where 