select s.name as employee , s.salary , d.name as department
from departments as d 
inner join staff as s on s.dept_id = d.id
order by d.name,s.salary;

select s.name as employee , s.salary , d.name as department
from staff as s
left join departments as d on s.dept_id = d.id
order by d.name,s.salary; -- it contains an extra row of null whose name is dev whose department name is null

select s.name , d.location 
from departments as d 
inner join staff as s on s.dept_id = d.id
where d.location = 'Mumbai';

select d.name , count(s.dept_id)
from departments as d 
left join staff as s on s.dept_id = d.id
group by d.name;

select d.name , round(avg(s.salary),2) as avg_sal
from departments as d 
left join staff as s on s.dept_id = d.id
group by d.name having round(avg(s.salary),2)>60000;

select d.name , count(s.dept_id) from departments as d 
left join staff as s on s.dept_id = d.id
group by d.name having count(s.dept_id)=0;
-- legal dept has no staff as the query showed legal with zero staff 

--challange
select d.name , d.location , count(s.dept_id) , coalesce(sum(s.salary), 0) as total_salary
from departments as d 
left join staff as s on s.dept_id = d.id
group by d.name ,d.location order by total_salary desc;
--coalesce is needed because without it legals total salary will show null and it is not a good output 
--so we use coalesce to provide null values a certain value according to our need 
 
--quiz 1)where is used to filter rows , having is used to filter groups and having can also use aggregates
--which where cant use 2)9 rows and dev will be lost as inner joins give rows which are common in both tables
--but dev does not have a dept_id 3)left join and keeping department at left side 4)we need aliases here because
-- we have used them to get the columns so if we dont declare these aliases then the code will give error 
-- and using aliases saves a lot of time  
--5) it is not possible for any value to have it as it is a primary key of that table and is always generated
-- so after left join it would mean that this is not matched by the correponding value on the table on the left side
-- and the left table is departments according to code provided