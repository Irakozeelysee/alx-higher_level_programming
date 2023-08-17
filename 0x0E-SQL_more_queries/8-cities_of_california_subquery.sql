-- Script to list all cities of California using a subquery

-- Switch to the specified database
USE hbtn_0d_usa;

SELECT id, name
FROM cities
WHERE state_id IN (
	SELECT id FROM states
	WHERE name = 'California')
ORDER BY id ASC;
