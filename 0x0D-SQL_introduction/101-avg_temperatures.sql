-- This script calculates the average temperature (Fahrenheit) by city and displays the results ordered by temperature (descending).

-- Calculate and list average temperature by city
SELECT city, AVG(temp_f) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
