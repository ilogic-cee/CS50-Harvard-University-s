-- Inserting sample data into tables

-- Insert data into Artist table
INSERT INTO Artist VALUES ('A1', 'Artist One', 'First1', 'Last1', 'Info about Artist One', 1000);
INSERT INTO Artist VALUES ('A2', 'Artist Two', 'First2', 'Last2', 'Info about Artist Two', 1500);
-- ... (add more artists as needed)

-- Insert data into Album table
INSERT INTO Album VALUES ('AL1', 'A1', 'Album One', TO_DATE('2021-01-01', 'YYYY-MM-DD'), 10);
INSERT INTO Album VALUES ('AL2', 'A2', 'Album Two', TO_DATE('2021-02-01', 'YYYY-MM-DD'), 8);
-- ... (add more albums as needed)

-- Insert data into Song table
INSERT INTO Song VALUES ('S1', 'A1', 'AL1', 'Song One', '3:30', 500, TO_DATE('2021-01-01', 'YYYY-MM-DD'));
INSERT INTO Song VALUES ('S2', 'A1', 'AL1', 'Song Two', '4:00', 300, TO_DATE('2021-01-15', 'YYYY-MM-DD'));
-- ... (add more songs as needed)

-- ... (similarly insert data into other tables like Music_Video, Playlist, etc.)

-- Retrieving data from tables

-- Get all songs by a specific artist
SELECT * FROM Song WHERE Artist = 'A1';

-- Get all albums by a specific artist
SELECT * FROM Album WHERE Artist = 'A1';

-- Get the total number of songs in each album
SELECT Album, COUNT(*) AS Total_Songs FROM Song GROUP BY Album;

-- Updating data in tables

-- Increase the number of shares for an artist
UPDATE Artist SET Shares = Shares + 500 WHERE Artist_ID = 'A1';

-- Update the duration of a specific song
UPDATE Song SET Duration = '4:30' WHERE Song_ID = 'S1';

-- Deleting data from tables

-- Delete a specific song
DELETE FROM Song WHERE Song_ID = 'S2';

-- Delete a specific album and its songs
DELETE FROM Song WHERE Album = 'AL2';
DELETE FROM Album WHERE Album_ID = 'AL2';

-- Complex Queries

-- Find artists with more than one album
SELECT Artist_ID, Stage_Name FROM Artist
WHERE Artist_ID IN (SELECT Artist FROM Album GROUP BY Artist HAVING COUNT(*) > 1);

-- List songs along with their artist names
SELECT Song.Title, Artist.Stage_Name FROM Song
JOIN Artist ON Song.Artist = Artist.Artist_ID;

-- Ensure to adapt and test these queries according to your database setup
