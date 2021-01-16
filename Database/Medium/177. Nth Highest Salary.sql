CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        
        Select distinct Salary from Employee
        order by Salary desc
        OFFSET @N - 1 rows
        fetch next 1 rows only
    );
END