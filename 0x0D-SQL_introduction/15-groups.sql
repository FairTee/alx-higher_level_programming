-- Script to list the number of records with the same score in the table second_table

-- Query to count the number of records for each score and display the result

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
