SELECT city, COUNT(*) FROM schools WHERE type = 'Public' GROUP BY city ORDER BY COUNT(*) DESC, city LIMIT 10;
SELECT city, COUNT(*) FROM schools WHERE type = 'Public' GROUP BY city HAVING COUNT(*) <= 3 ORDER BY COUNT(*) DESC, city;
