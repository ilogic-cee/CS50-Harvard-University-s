SELECT name FROM districts WHERE number_of_pupils = (SELECT MIN(number_of_pupils) FROM districts);
