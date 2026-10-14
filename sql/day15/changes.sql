select name , salary from employees where id = 8; --1
update employees set salary = 45000 where id = 8;
select name , salary from employees where id = 8 ;

select name , salary from employees where department = 'Support'; --2
update employees set salary = salary * 1.10 where department = 'Support';
select name , salary from employees where department = 'Support';

select name , city from employees where city is NULL; --3
update employees set city ='Remote' where city is NULL;
select name , city from employees where city = 'Remote';

select * from employees where id = 5; --4
update employees set department = 'Sales' , city = 'Noida' where id = 5;
select * from employees where id = 5;

select * from employees where id = 12; --5
delete from employees where id = 12;
select * from employees where id = 12;

select * from employees where hire_date < '2020-01-01'; --6
delete from employees where hire_date < '2020-01-01';
select * from employees;