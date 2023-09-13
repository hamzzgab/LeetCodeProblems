# Write your MySQL query statement below
SELECT      E2.employee_id, 
            E2.name, 
            COUNT(*) as reports_count,
            ROUND(AVG(E1.age)) as average_age
FROM        Employees E1
INNER JOIN  Employees E2
ON          E1.reports_to = E2.employee_id
GROUP BY    E2.employee_id, E2.name
ORDER BY    E2.employee_id
