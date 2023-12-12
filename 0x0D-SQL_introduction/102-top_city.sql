-- This script displays the top 3 cities' temperatures during July and August ordered by temperature in descending order.

-- Select the city and the average temperature for each city during the months of July (7) and August (8).
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
-- Order the results by average temperature in descending order.
ORDER BY avg_temp DESC
-- Limit the output to the top 3 cities.
LIMIT 3;
