# Write your MySQL query statement below
SELECT E1.name as Employee from Employee E1
INNER JOIN Employee E2
ON E1.managerId = E2.id
WHERE E1.salary > E2.salary