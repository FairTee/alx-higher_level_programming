-- This script displays the maximum temperature of each state, ordered by state name.

-- Select the state, and the maximum temperature for each state.

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
