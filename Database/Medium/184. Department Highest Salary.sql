select Department , Employee , Salary from 
(
select a.Name as 'Employee' , 
       b.Name as 'Department',
       Salary,
       RANK() OVER(partition by a.DepartmentId order by Salary desc ) as rnk
from Employee a
join Department b
on a.DepartmentId = b.Id
) as tt
where rnk = 1 ;



/* Second Way- works in MySQL*/

select a.Name as 'Employee' , 
       b.Name as 'Department',
       Salary
from Employee a
join Department b
on a.DepartmentId = b.Id
where (Salary,DepartmentId) in (select max(Salary) , DepartmentId from Employee group by DepartmentId)

