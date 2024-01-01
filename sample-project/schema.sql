DROP TABLE Artist
CASCADE CONSTRAINTS;
DROP TABLE Artist_Concert
CASCADE CONSTRAINTS;
DROP TABLE Song
CASCADE CONSTRAINTS;
DROP TABLE Song_Genre
CASCADE CONSTRAINTS;
DROP TABLE Music_Video
CASCADE CONSTRAINTS;
DROP TABLE Album
CASCADE CONSTRAINTS;
DROP TABLE Album_Genre
CASCADE CONSTRAINTS;
DROP TABLE Playlist
CASCADE CONSTRAINTS;
DROP TABLE Song_on_Playlist
CASCADE CONSTRAINTS;
DROP TABLE Artist_on_Playlist
CASCADE CONSTRAINTS;
DROP TABLE SUser
CASCADE CONSTRAINTS;

CREATE TABLE Artist
(
    Artist_ID VARCHAR2(20),
    Stage_Name VARCHAR2(20),
    First_Name VARCHAR2(20),
    Last_Name VARCHAR2(250),
    Artist_Info VARCHAR2(20),
    Shares NUMBER(20),
    CONSTRAINT artist_pk PRIMARY KEY (Artist_ID)
);



CREATE TABLE Artist_Concert
(
    Artist VARCHAR2(20),
    Venue VARCHAR2(20),
    Date_Con DATE,
    Time VARCHAR2(20),
    CONSTRAINT artist_concert_pk PRIMARY KEY (Artist)
);

CREATE TABLE Song
(
    Song_ID VARCHAR2(30),
    Artist VARCHAR2(20),
    Album VARCHAR2(30),
    Title VARCHAR2(30),
    Duration VARCHAR2(20),
    Number_of_Plays VARCHAR2(20),
    Release_Date DATE,
    CONSTRAINT song_pk PRIMARY KEY (Song_ID)
);

CREATE TABLE Song_Genre
(
    Song VARCHAR2(30),
    Song_Genre VARCHAR2(30),
    CONSTRAINT song_genre_pk PRIMARY KEY (Song, Song_Genre)
);

CREATE TABLE Music_Video
(
    Video_ID VARCHAR2(20),
    Song VARCHAR2(20),
    Title VARCHAR2(20),
    Duration VARCHAR2(20),
    Release_Date DATE,
    CONSTRAINT music_video_pk PRIMARY KEY (Video_ID)
);

CREATE TABLE Album
(
    Album_ID VARCHAR2(30),
    Artist VARCHAR2(20),
    Title VARCHAR2(30),
    Release_Date DATE,
    Number_of_Songs VARCHAR2(20),
    CONSTRAINT album_pk PRIMARY KEY (Album_ID)
);

CREATE TABLE Album_Genre
(
    Album VARCHAR2(20),
    Album_Genre VARCHAR2(20),
    CONSTRAINT album_genre_pk PRIMARY KEY (Album, Album_Genre)
);


CREATE TABLE Playlist
(
    Playlist_ID VARCHAR2(20),
    Number_of_Songs VARCHAR2(20),
    Title VARCHAR2(20),
    Created_By VARCHAR2(20),
    CONSTRAINT playlist_pk PRIMARY KEY (Playlist_ID)
);

CREATE TABLE Song_on_Playlist
(
    Song VARCHAR2(20),
    Playlist VARCHAR2(20),
    Date_Added VARCHAR2(20),
    CONSTRAINT song_on_playlist_pk PRIMARY KEY (Song)
);

CREATE TABLE Artist_on_Playlist
(
    Artist VARCHAR2(20),
    Playlist VARCHAR2(20),
    Date_Added VARCHAR2(20),
    CONSTRAINT artist_on_playlist_pk PRIMARY KEY (Artist)
);

CREATE TABLE SUser
(
    Username VARCHAR2(20),
    Age VARCHAR2(20),
    Country VARCHAR2(20),
    Email VARCHAR2(20),
    CONSTRAINT suser_pk PRIMARY KEY (Username)
);

ALTER TABLE Artist_Concert
ADD CONSTRAINT artist_concert_fk FOREIGN KEY (Artist)
REFERENCES Artist (Artist_ID);

ALTER TABLE Song
ADD CONSTRAINT song_fk FOREIGN KEY (Artist)
REFERENCES Artist (Artist_ID);

ALTER TABLE Song
ADD CONSTRAINT song_fk2 FOREIGN KEY (Album)
REFERENCES Album (Album_ID);

ALTER TABLE Song_Genre
ADD CONSTRAINT song_genre_fk FOREIGN KEY (Song)
REFERENCES Song (Song_ID);

ALTER TABLE Music_Video
ADD CONSTRAINT music_video_fk FOREIGN KEY (Song)
REFERENCES Song (Song_ID);

ALTER TABLE Album
ADD CONSTRAINT album_fk FOREIGN KEY (Artist)
REFERENCES Artist (Artist_ID);

ALTER TABLE Album_Genre
ADD CONSTRAINT album_genre_fk FOREIGN KEY (Album)
REFERENCES Album (Album_ID);

ALTER TABLE Song_on_Playlist
ADD CONSTRAINT song_on_playlist_fk FOREIGN KEY (Song)
REFERENCES Song (Song_ID);

ALTER TABLE Song_on_Playlist
ADD CONSTRAINT song_on_playlist_fk2 FOREIGN KEY (Playlist)
REFERENCES Playlist (Playlist_ID);

ALTER TABLE Artist_on_Playlist
ADD CONSTRAINT artist_on_playlist_fk FOREIGN KEY (Artist)
REFERENCES Artist (Artist_ID);

ALTER TABLE Artist_on_Playlist
ADD CONSTRAINT artist_on_playlist_fk2 FOREIGN KEY (Playlist)
REFERENCES Playlist (Playlist_ID);

ALTER TABLE Playlist
ADD CONSTRAINT playlist_fk FOREIGN KEY (Created_By)
REFERENCES SUser (Username);

/*Each table needs at least 10 tuples, need 400 total tuples*/

/*Artist (Artist_ID, Stage_Name, First_Name, Last_Name, Artist_Info, Shares) tuples*/
INSERT INTO Artist
VALUES
    ('Tipper', 'Tipper', 'Dave', 'Tipper', 'DJ/Producer', '1000000');

INSERT INTO Artist
VALUES
    ('Drake', 'Drake', 'Aubrey', 'Graham', 'Rapper', '1000000');

INSERT INTO Artist
VALUES
    ('Kursa', 'Kursa', 'Not_Given', 'Not_Given', 'DJ/Producer', '1000000');

INSERT INTO Artist
VALUES
    ('Opiou', 'Opiou', 'Not_Given', 'Not_Given', 'DJ/Producer', '1000000');

INSERT INTO Artist
VALUES
    ('Ed_Sheeran', 'Ed Sheeran', 'Ed', 'Sheeran', 'Singer/Songwriter', '1000000');

INSERT INTO Artist
VALUES
    ('Eprom', 'Eprom', 'Alexander', 'Dennis', 'DJ/Producer', '531837');

INSERT INTO Artist
VALUES
    ('Kanye_West', 'Kanye West', 'Kanye', 'West', 'Rapper', '1000000');

INSERT INTO Artist
VALUES
    ('Bassnectar', 'Bassnectar', 'Lorin', 'Ashton', 'DJ/Producer', '1933987');

INSERT INTO Artist
VALUES
    ('Avicii', 'Avicii', 'Tim', 'Berling', 'DJ/Producer', '1000000');

INSERT INTO Artist
VALUES
    ('Khalid', 'Khalid', 'Khalid', 'Robinson', 'Singer', '1000000');

INSERT INTO Artist
VALUES
    ('Porter_Robinson', 'Porter Robinson', 'Porter', 'Robinson', 'DJ/Producer', '1474363');

/*Artist_Concert (Artist, Venue, Date_Con, Time) tuples*/


/*Music_Video (Video_ID, Song, Title, Duration, Release_Date) tuples*/

/*Album (Album_ID, Artist, Title, Release_Date, Num_Songs) tuples*/
INSERT INTO Album
VALUES
    ('Forward_Escape', 'Tipper', 'Forward Escape', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'), 11);

INSERT INTO Album
VALUES
    ('Nothing_Was_The_Same', 'Drake', 'Nothing Was The Same', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'), 11);

INSERT INTO Album
VALUES
    ('Waerbl', 'Kursa', 'Waerbl', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'), 11);

INSERT INTO Album
VALUES
    ('Omniversal', 'Opiou', 'Omniversal', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'), 11);

INSERT INTO Album
VALUES
    ('x', 'Ed_Sheeran', 'x', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'), 11);

INSERT INTO Album
VALUES
    ('Halflife', 'Eprom', 'Halflife', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'), 11);

INSERT INTO Album
VALUES
    ('Graduation', 'Kanye_West', 'Graduation', TO_DATE('2007/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'), 11);

INSERT INTO Album
VALUES
    ('Into_the_Sun', 'Bassnectar', 'Into the Sun', TO_DATE('2015/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'), 11);

INSERT INTO Album
VALUES
    ('True', 'Avicii', 'True', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'), 11);

INSERT INTO Album
VALUES
    ('American_Teen', 'Khalid', 'American Teen', TO_DATE('2017/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'), 11);

INSERT INTO Album
VALUES
    ('Worlds', 'Porter_Robinson', 'Worlds', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'), 11);

/*Album_Genre tuples (Album, Album_Genre)*/

/*Song tuples (Song_ID, Artist, Album, Title, Duration, Num_plays, Release_date)*/
/*Tipper - Forward Escape*/
INSERT INTO Song
VALUES
    ('Portal_Spillage', 'Tipper', 'Forward_Escape', 'Portal Spillage', '3:01', '2331648', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Dreamsters', 'Tipper', 'Forward_Escape', 'Dreamsters', '5:29', '2331648', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Homage_Sliders', 'Tipper', 'Forward_Escape', 'Homage Sliders', '5:01', '2331648', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Table_Flipping', 'Tipper', 'Forward_Escape', 'Table Flipping', '4:23', '2331648', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Gulch', 'Tipper', 'Forward_Escape', 'Gulch', '3:57', '2331648', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Grabbers_Holders', 'Tipper', 'Forward_Escape', 'Grabbers_Holders', '4:37', '2331648', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('The_Bedraggling', 'Tipper', 'Forward_Escape', 'The Bedraggling', '4:08', '2331648', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('The_Re_Up', 'Tipper', 'Forward_Escape', 'The Re-Up', '3:53', '2331648', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Apex_of_the_Vortex', 'Tipper', 'Forward_Escape', 'Apex of the Vortex', '2:24', '2331648', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Rip_Cord', 'Tipper', 'Forward_Escape', 'Rip Cord', '6:12', '2331648', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Reverse_Dross_Maneuver', 'Tipper', 'Forward_Escape', 'Reverse Dross Maneuver', '5:42', '2331648', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

/*Drake - Nothing Was The Same*/
INSERT INTO Song
VALUES
    ('Tuscan_leather', 'Drake', 'Nothing_Was_The_Same', 'Tuscan Leather', '6:06', '1000000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Furthest_Thing', 'Drake', 'Nothing_Was_The_Same', 'Furthest Thing', '4:27', '1000000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Started_from_the_Bottom', 'Drake', 'Nothing_Was_The_Same', 'Started from the Bottom', '2:54', '1000000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Wu_Tang_Forever', 'Drake', 'Nothing_Was_The_Same', 'Wu-Tang Forever', '3:38', '1000000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Own_It', 'Drake', 'Nothing_Was_The_Same', 'Own it', '4:12', '1000000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Worst_Behavior', 'Drake', 'Nothing_Was_The_Same', 'Worst Behavior', '4:30', '1000000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('From_Time', 'Drake', 'Nothing_Was_The_Same', 'From Time', '5:22', '1000000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Hold_On_Were_Going_Home', 'Drake', 'Nothing_Was_The_Same', 'Hold On, Were Going Home', '3:48', '1000000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Connect', 'Drake', 'Nothing_Was_The_Same', 'Connect', '4:56', '1000000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('The_Language', 'Drake', 'Nothing_Was_The_Same', 'The Language', '3:44', '1000000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('305_To_My_City', 'Drake', 'Nothing_Was_The_Same', '305 To My City', '4:16', '1000000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

/*Kursa - Waerbl*/
INSERT INTO Song
VALUES
    ('Waking', 'Kursa', 'Waerbl', 'Waking', '3:15', '500000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Waerbl', 'Kursa', 'Waerbl', 'Waerbl', '3:55', '500000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Scratch_Hop', 'Kursa', 'Waerbl', 'Scratch Hop', '2:40', '500000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Maybe', 'Kursa', 'Waerbl', 'Maybe', '4:36', '500000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('No_More_Bad_Dreams', 'Kursa', 'Waerbl', 'No More Bad Dreams', '3:06', '500000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Nightmares', 'Kursa', 'Waerbl', 'Nightmares', '3:17', '500000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Anuva', 'Kursa', 'Waerbl', 'Anuva', '4:11', '500000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Interlude', 'Kursa', 'Waerbl', 'Interlude', '2:49', '500000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('A_Little_Different', 'Kursa', 'Waerbl', 'A Little Different', '4:41', '500000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('No_Reality', 'Kursa', 'Waerbl', 'No Reality', '6:01', '500000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Underneat', 'Kursa', 'Waerbl', 'Underneat', '5:57', '500000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

/*Opiou - Omniversal*/
INSERT INTO Song
VALUES
    ('Huxley_Hustle', 'Opiou', 'Omniversal', 'Huxley Hustle', '5:43', '250000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Sneakers', 'Opiou', 'Omniversal', 'Sneakers', '5:16', '250000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Waxomole', 'Opiou', 'Omniversal', 'Waxomole', '4:57', '250000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Flanjitsu', 'Opiou', 'Omniversal', 'Flanjitsu', '5:01', '250000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Paint_the_World', 'Opiou', 'Omniversal', 'Paint the World', '3:09', '250000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Jelly', 'Opiou', 'Omniversal', 'Jelly', '4:07', '250000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('The_Pepper', 'Opiou', 'Omniversal', 'The Pepper', '4:31', '250000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Kurdilly', 'Opiou', 'Omniversal', 'Kurdilly', '6:00', '250000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Airy_Watson', 'Opiou', 'Omniversal', 'Airy Watson', '3:43', '250000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Pumpernickel', 'Opiou', 'Omniversal', 'Pumpernickel', '5:14', '250000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Axolotl_Throttle', 'Opiou', 'Omniversal', 'Axolotl Throttle', '4:58', '250000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

/*Ed Sheeran - x*/
INSERT INTO Song
VALUES
    ('One', 'Ed_Sheeran', 'x', 'One', '4:13', '2000000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Im_a_Mess', 'Ed_Sheeran', 'x', 'Im a Mess', '4:05', '2000000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Sing', 'Ed_Sheeran', 'x', 'Sing', '3:55', '2000000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Dont', 'Ed_Sheeran', 'x', 'Dont', '3:40', '2000000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Nina', 'Ed_Sheeran', 'x', 'Nina', '3:46', '2000000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Photograph', 'Ed_Sheeran', 'x', 'Photograph', '4:19', '2000000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Bloodstream', 'Ed_Sheeran', 'x', 'Bloodstream', '5:00', '2000000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Tenerife_Sea', 'Ed_Sheeran', 'x', 'Tenerife Sea', '4:01', '2000000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Runaway', 'Ed_Sheeran', 'x', 'Runaway', '3:25', '2000000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('The_Man', 'Ed_Sheeran', 'x', 'The Man', '4:10', '2000000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Thinking_out_Loud', 'Ed_Sheeran', 'x', 'Thinking out Loud', '4:42', '2000000', TO_DATE('2016/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

/*Eprom - Halflife*/
INSERT INTO Song
VALUES
    ('Center_of_the_Sun', 'Eprom', 'Halflife', 'Center of the Sun', '3:20', '200000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Beasts_of_Babylon', 'Eprom', 'Halflife', 'Beasts of Babylon', '2:44', '200000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Hurricane', 'Eprom', 'Halflife', 'Hurricane', '2:43', '200000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Vogel', 'Eprom', 'Halflife', 'Vogel', '3:26', '200000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Super_FX', 'Eprom', 'Halflife', 'Super FX', '3:12', '200000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Lost_Levels', 'Eprom', 'Halflife', 'Lost Levels', '2:08', '200000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Screwface', 'Eprom', 'Halflife', 'Screwface', '3:37', '200000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Machine_Skin', 'Eprom', 'Halflife', 'Machine Skin', '5:17', '200000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Pentatonic_Dust', 'Eprom', 'Halflife', 'Pentatonic Dust', '1:20', '200000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Moisture', 'Eprom', 'Halflife', 'Moisture', '2:08', '200000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Turtle_Ride', 'Eprom', 'Halflife', 'Turtle Ride', '2:11', '200000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

/*Kanye West - Graduation*/
INSERT INTO Song
VALUES
    ('Good_Morning', 'Kanye_West', 'Graduation', 'Good Morning', '3:15', '200000', TO_DATE('2007/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Champion', 'Kanye_West', 'Graduation', 'Champion', '2:48', '200000', TO_DATE('2007/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Stronger', 'Kanye_West', 'Graduation', 'Stronger', '5:12', '200000', TO_DATE('2007/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('I_Wonder', 'Kanye_West', 'Graduation', 'I Wonder', '4:03', '200000', TO_DATE('2007/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Good_Life', 'Kanye_West', 'Graduation', 'Good Life', '3:27', '200000', TO_DATE('2007/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Cant_Tell_Me_Nothing', 'Kanye_West', 'Graduation', 'Cant Tell Me Nothing', '4:32', '200000', TO_DATE('2007/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Barry_Bonds', 'Kanye_West', 'Graduation', 'Barry Bonds', '3:24', '200000', TO_DATE('2007/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Drunk_and_Hot_Girls', 'Kanye_West', 'Graduation', 'Drunk and Hot Girls', '5:13', '200000', TO_DATE('2007/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Flashing_Lights', 'Kanye_West', 'Graduation', 'Flashing Lights', '3:58', '200000', TO_DATE('2007/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Everything_I_Am', 'Kanye_West', 'Graduation', 'Everything I Am', '3:48', '200000', TO_DATE('2007/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('The_Glory', 'Kanye_West', 'Graduation', 'The Glory', '3:33', '200000', TO_DATE('2007/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

/*Bassnectar - Into the Sun*/
INSERT INTO Song
VALUES
    ('Chasing_Heaven', 'Bassnectar', 'Into_the_Sun', 'Chasing Heaven', '5:19', '780000', TO_DATE('2015/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Into_the_Sun', 'Bassnectar', 'Into_the_Sun', 'Into the Sun', '4:16', '780000', TO_DATE('2015/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Speakerbox', 'Bassnectar', 'Into_the_Sun', 'Speakerbox', '4:42', '780000', TO_DATE('2015/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('The_Mystery_Spot', 'Bassnectar', 'Into_the_Sun', 'The Mystery Spot', '4:30', '780000', TO_DATE('2015/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Sideways', 'Bassnectar', 'Into_the_Sun', 'Sideways', '3:04', '780000', TO_DATE('2015/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Rose_Colored_Bass', 'Bassnectar', 'Into_the_Sun', 'Rose Colored Bass', '3:43', '780000', TO_DATE('2015/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Generate', 'Bassnectar', 'Into_the_Sun', 'Generate', '3:42', '780000', TO_DATE('2015/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('One_Thing', 'Bassnectar', 'Into_the_Sun', 'One Thing', '3:44', '780000', TO_DATE('2015/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Science_Fiction', 'Bassnectar', 'Into_the_Sun', 'Science Fiction', '5:13', '780000', TO_DATE('2015/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Blow', 'Bassnectar', 'Into_the_Sun', 'Blow', '4:01', '780000', TO_DATE('2015/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Sommarfagel', 'Bassnectar', 'Into_the_Sun', 'Sommarfagel', '2:17', '780000', TO_DATE('2015/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

/*Avicii - True*/
INSERT INTO Song
VALUES
    ('Wake_Me_Up', 'Avicii', 'True', 'Wake Me Up', '4:07', '780000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('You_Make_Me', 'Avicii', 'True', 'You Make Me', '3:53', '780000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Hey_Brother', 'Avicii', 'True', 'Hey Brother', '4:15', '780000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Addicted_To_You', 'Avicii', 'True', 'Addicted To You', '2:28', '780000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Dear_Boy', 'Avicii', 'True', 'Dear Boy', '7:59', '780000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Liar_Liar', 'Avicii', 'True', 'Liar Liar', '3:59', '780000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Shame_On_Me', 'Avicii', 'True', 'Shame on Me', '4:11', '780000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Lay_Me_Down', 'Avicii', 'True', 'Lay Me Down', '5:00', '780000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Hope_Theres_Someone', 'Avicii', 'True', 'Hope Theres Someone', '6:21', '780000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Heart_Upon_My_Sleeve', 'Avicii', 'True', 'Heart Upon My Sleeve', '4:43', '780000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Canyons', 'Avicii', 'True', 'Canyons', '7:29', '780000', TO_DATE('2013/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

/*Khalid - American Teen*/
INSERT INTO Song
VALUES
    ('American_Teen', 'Khalid', 'American_Teen', 'American Teen', '4:11', '780000', TO_DATE('2017/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Young_Dumb_and_Brokee', 'Khalid', 'American_Teen', 'Young Dumb and Brokee', '3:23', '780000', TO_DATE('2017/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Location', 'Khalid', 'American_Teen', 'Location', '3:39', '780000', TO_DATE('2017/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Another_Sad_Love_Song', 'Khalid', 'American_Teen', 'Another Sad Love Song', '4:05', '780000', TO_DATE('2017/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Saved', 'Khalid', 'American_Teen', 'Saved', '3:27', '780000', TO_DATE('2017/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Coaster', 'Khalid', 'American_Teen', 'Coaster', '3:19', '780000', TO_DATE('2017/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('8TEEN', 'Khalid', 'American_Teen', '8TEEN', '3:49', '780000', TO_DATE('2017/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Lets_Go', 'Khalid', 'American_Teen', 'Lets Go', '3:25', '780000', TO_DATE('2017/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Hopeless', 'Khalid', 'American_Teen', 'Hopelss', '2:48', '780000', TO_DATE('2017/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Cold_Blooded', 'Khalid', 'American_Teen', 'Cold Blooded', '3:28', '780000', TO_DATE('2017/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Winter', 'Khalid', 'American_Teen', 'Winter', '4:02', '780000', TO_DATE('2017/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

/*Porter Robinson - Worlds*/
INSERT INTO Song
VALUES
    ('Divinity', 'Porter_Robinson', 'Worlds', 'Divinity', '6:08', '7800000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Sad_Machine', 'Porter_Robinson', 'Worlds', 'Sad Machine', '5:51', '7800000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Years_of_War', 'Porter_Robinson', 'Worlds', 'Years of War', '3:56', '7800000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Flicker', 'Porter_Robinson', 'Worlds', 'Flicker', '4:39', '7800000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Fresh_Static_Snow', 'Porter_Robinson', 'Worlds', 'Fresh Static Snow', '5:59', '7800000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Polygon_Dust', 'Porter_Robinson', 'Worlds', 'Polygon Dust', '3:29', '7800000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Hear_The_Bells', 'Porter_Robinson', 'Worlds', 'Hear The Bells', '4:47', '7800000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Natural_Light', 'Porter_Robinson', 'Worlds', 'Natural Light', '2:21', '7800000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Lionhearted', 'Porter_Robinson', 'Worlds', 'Lionhearted', '4:26', '7800000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Sea_Of_Voices', 'Porter_Robinson', 'Worlds', 'Sea of Voices', '4:59', '7800000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

INSERT INTO Song
VALUES
    ('Fellow_Feeling', 'Porter_Robinson', 'Worlds', 'Fellow Feeling', '5:50', '7800000', TO_DATE('2014/01/01 08:30:00', 'yyyy/mm/dd hh24:mi:ss'));

/*Song_Genre tuples (Song, Song_Genre)*/
/*Tipper - Forward Escape*/
INSERT INTO Song_Genre
VALUES
    ('Portal_Spillage', 'IDM');
INSERT INTO Song_Genre
VALUES
    ('Dreamsters', 'IDM');
INSERT INTO Song_Genre
VALUES
    ('Homage_Sliders', 'IDM');
INSERT INTO Song_Genre
VALUES
    ('Table_Flipping', 'IDM');
INSERT INTO Song_Genre
VALUES
    ('Gulch', 'IDM');
INSERT INTO Song_Genre
VALUES
    ('Grabbers_Holders', 'IDM');
INSERT INTO Song_Genre
VALUES
    ('The_Bedraggling', 'IDM');
INSERT INTO Song_Genre
VALUES
    ('The_Re_Up', 'IDM');
INSERT INTO Song_Genre
VALUES
    ('Apex_of_the_Vortex', 'IDM');
INSERT INTO Song_Genre
VALUES
    ('Rip_Cord', 'IDM');
INSERT INTO Song_Genre
VALUES
    ('Reverse_Dross_Maneuver', 'IDM');

/*Drake - Nothing Was The Same*/
INSERT INTO Song_Genre
VALUES
    ('Tuscan_leather', 'Hip-Hop/Rap');
INSERT INTO Song_Genre
VALUES
    ('Furthest_Thing', 'Hip-Hop/Rap');
INSERT INTO Song_Genre
VALUES
    ('Started_from_the_Bottom', 'Hip-Hop/Rap');
INSERT INTO Song_Genre
VALUES
    ('Wu_Tang_Forever', 'Hip-Hop/Rap');
INSERT INTO Song_Genre
VALUES
    ('Own_It', 'Hip-Hop/Rap');
INSERT INTO Song_Genre
VALUES
    ('Worst_Behavior', 'Hip-Hop/Rap');
INSERT INTO Song_Genre
VALUES
    ('From_Time', 'Hip-Hop/Rap');
INSERT INTO Song_Genre
VALUES
    ('Hold_On_Were_Going_Home', 'Hip-Hop/Rap');
INSERT INTO Song_Genre
VALUES
    ('Connect', 'Hip-Hop/Rap');
INSERT INTO Song_Genre
VALUES
    ('The_Language', 'Hip-Hop/Rap');
INSERT INTO Song_Genre
VALUES
    ('305_To_My_City', 'Hip-Hop/Rap');

/*Kursa - Waerbl*/
INSERT INTO Song_Genre
VALUES
    ('Waking', 'EDM/Space_Bass/Neuro');
INSERT INTO Song_Genre
VALUES
    ('Waerbl', 'EDM/Space_Bass/Neuro');
INSERT INTO Song_Genre
VALUES
    ('Scratch_Hop', 'EDM/Space_Bass/Neuro');
INSERT INTO Song_Genre
VALUES
    ('Maybe', 'EDM/Space_Bass/Neuro');
INSERT INTO Song_Genre
VALUES
    ('No_More_Bad_Dreams', 'EDM/Space_Bass/Neuro');
INSERT INTO Song_Genre
VALUES
    ('Nightmares', 'EDM/Space_Bass/Neuro');
INSERT INTO Song_Genre
VALUES
    ('Anuva', 'EDM/Space_Bass/Neuro');
INSERT INTO Song_Genre
VALUES
    ('Interlude', 'EDM/Space_Bass/Neuro');
INSERT INTO Song_Genre
VALUES
    ('A_Little_Different', 'EDM/Space_Bass/Neuro');
INSERT INTO Song_Genre
VALUES
    ('No_Reality', 'EDM/Space_Bass/Neuro');
INSERT INTO Song_Genre
VALUES
    ('Underneat', 'EDM/Space_Bass/Neuro');

/*Opiou - Omniversal*/
INSERT INTO Song_Genre
VALUES
    ('Huxley_Hustly', 'EDM/Funk');
INSERT INTO Song_Genre
VALUES
    ('Huxley_Hustly', 'EDM/Funk');
INSERT INTO Song_Genre
VALUES
    ('Huxley_Hustly', 'EDM/Funk');
INSERT INTO Song_Genre
VALUES
    ('Huxley_Hustly', 'EDM/Funk');
INSERT INTO Song_Genre
VALUES
    ('Huxley_Hustly', 'EDM/Funk');
INSERT INTO Song_Genre
VALUES
    ('Huxley_Hustly', 'EDM/Funk');
INSERT INTO Song_Genre
VALUES
    ('Huxley_Hustly', 'EDM/Funk');
INSERT INTO Song_Genre
VALUES
    ('Huxley_Hustly', 'EDM/Funk');
INSERT INTO Song_Genre
VALUES
    ('Huxley_Hustly', 'EDM/Funk');
INSERT INTO Song_Genre
VALUES
    ('Huxley_Hustly', 'EDM/Funk');
INSERT INTO Song_Genre
VALUES
    ('Huxley_Hustly', 'EDM/Funk');
/*Playlist (Playlist_ID, Num_Songs, Title, Created_by) tuples*/

/*Song_on_Playlist (Song, Playlist, Date_Added) tuples*/

/*Artist_on_Playlist (Artist, Playlist, Date_Added) tuples*/

/*SUser (Username, Age, Country, Email)*/

SELECT Artist_ID, First_Name, Shares
FROM Artist;

SELECT Song_ID, Artist
FROM Song;

SELECT Album_ID, Artist, Release_Date
FROM Album;

SELECT Song, Song_Genre
FROM Song_Genre;
