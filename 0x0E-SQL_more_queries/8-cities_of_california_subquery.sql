-- 8-cities_of_california_subquery.sql

-- Use the hbtn_0d_usa database.
USE hbtn_0d_usa;

-- Select the cities of California
SELECT id, name
FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
