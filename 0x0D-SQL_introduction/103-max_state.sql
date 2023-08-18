-- Query to display max temperature of each state

SELECT state, MAX(value) AS max_temp FROM Temperatures
GROUP BY state
ORDER BY state;
