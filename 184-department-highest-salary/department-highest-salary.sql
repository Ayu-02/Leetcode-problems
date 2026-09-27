# Write your MySQL query statement below
SELECT d.name AS Department,
e.name AS Employee,
e.Salary As Salary
FROM Employee e
join Department d ON e.departmentId=d.id
WHERE e.Salary =(
SELECT MAX(salary)
FROM Employee
WHERE departmentId = e.departmentId
);