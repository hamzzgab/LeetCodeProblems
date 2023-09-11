# Write your MySQL query statement below
SELECT e.name as Employee from Employee e
WHERE e.salary > (SELECT m.salary from Employee as m WHERE m.id = e.managerId)