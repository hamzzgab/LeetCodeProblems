# Write your MySQL query statement below
UPDATE 	Salary 
SET 	Sex =  CASE  
                        WHEN SEX = 'm' THEN 'f' 
                        WHEN SEX = 'f' THEN 'm'
                        ELSE SEX
                    END 
WHERE   SEX IN ('m', 'f');