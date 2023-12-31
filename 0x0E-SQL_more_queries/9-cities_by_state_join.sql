-- Select cities and their corresponding states

SELECT cities.id, cities.name AS city_name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
