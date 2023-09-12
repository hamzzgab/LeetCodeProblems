# Write your MySQL query statement below
UPDATE 	Salary 
SET 	Sex =  CASE  
                        WHEN SEX = 'm' THEN 'f' 
                        ELSE 'm'
                    END 
WHERE   SEX IN ('m', 'f');