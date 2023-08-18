-- Query to display top 3 cities with highest average

SELECT city, AVG(temperature) AS avg_temp
FROM Temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
