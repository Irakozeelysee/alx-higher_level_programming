-- Script to list all genres and their linked show counts

SELECT tv_genres.genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
