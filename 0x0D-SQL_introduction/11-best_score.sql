-- Script to list records with a score >= 10 in the table second_table

-- Query to retrieve records with score >= 10 from second_table, ordered by score

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
