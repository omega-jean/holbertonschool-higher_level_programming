-- 0x0D. SQL - Introduction, task 16. Say my name
-- script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC;