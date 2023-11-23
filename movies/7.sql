SELECT m.title, r r.rating FROM movies m
JOIN ratings r ON m.id = r.movie_id
WHERE m. year = 2010
ORDER BY r rating DECS, m. title ASC;
