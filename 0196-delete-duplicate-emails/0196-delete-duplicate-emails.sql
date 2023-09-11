# Write your MySQL query statement below
DELETE p FROM Person p, Person P2 WHERE p.email = P2.email and p.id > P2.id;