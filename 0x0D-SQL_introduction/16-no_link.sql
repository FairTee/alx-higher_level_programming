-- Script to list all records of the table second_table excluding rows without a name value


-- Query to retrieve records with a name value, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
