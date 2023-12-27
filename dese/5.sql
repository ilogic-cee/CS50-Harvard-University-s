SELECT city, COUNT(*) FROM schools WHERE type = 'Public' GROUP BY city HAVING COUNT(*) <= 3 ORDER BY COUNT(*) DESC, city;
