-- Drop existing tables if they exist
DROP TABLE Artist CASCADE CONSTRAINTS;
DROP TABLE Artist_Concert CASCADE CONSTRAINTS;
DROP TABLE Song CASCADE CONSTRAINTS;
DROP TABLE Song_Genre CASCADE CONSTRAINTS;
DROP TABLE Music_Video CASCADE CONSTRAINTS;
DROP TABLE Album CASCADE CONSTRAINTS;
DROP TABLE Album_Genre CASCADE CONSTRAINTS;
DROP TABLE Playlist CASCADE CONSTRAINTS;
DROP TABLE Song_on_Playlist CASCADE CONSTRAINTS;
DROP TABLE Artist_on_Playlist CASCADE CONSTRAINTS;
DROP TABLE SUser CASCADE CONSTRAINTS;

-- Create Artist table
CREATE TABLE Artist (
    Artist_ID VARCHAR2(20),
    Stage_Name VARCHAR2(20),
    First_Name VARCHAR2(20),
    Last_Name VARCHAR2(250),
    Artist_Info VARCHAR2(20),
    Shares NUMBER(20),
    CONSTRAINT artist_pk PRIMARY KEY (Artist_ID)
);

-- Create Artist_Concert table
CREATE TABLE Artist_Concert (
    Artist VARCHAR2(20),
    Venue VARCHAR2(20),
    Date_Con DATE,
    Time VARCHAR2(20),
    CONSTRAINT artist_concert_pk PRIMARY KEY (Artist)
);

-- Create Song table
CREATE TABLE Song (
    Song_ID VARCHAR2(30),
    Artist VARCHAR2(20),
    Album VARCHAR2(30),
    Title VARCHAR2(30),
    Duration VARCHAR2(20),
    Number_of_Plays VARCHAR2(20),
    Release_Date DATE,
    CONSTRAINT song_pk PRIMARY KEY (Song_ID)
);

-- Create Song_Genre table
CREATE TABLE Song_Genre (
    Song VARCHAR2(30),
    Song_Genre VARCHAR2(30),
    CONSTRAINT song_genre_pk PRIMARY KEY (Song, Song_Genre)
);

-- Create Music_Video table
CREATE TABLE Music_Video (
    Video_ID VARCHAR2(20),
    Song VARCHAR2(20),
    Title VARCHAR2(20),
    Duration VARCHAR2(20),
    Release_Date DATE,
    CONSTRAINT music_video_pk PRIMARY KEY (Video_ID)
);

-- Create Album table
CREATE TABLE Album (
    Album_ID VARCHAR2(30),
    Artist VARCHAR2(20),
    Title VARCHAR2(30),
    Release_Date DATE,
    Number_of_Songs VARCHAR2(20),
    CONSTRAINT album_pk PRIMARY KEY (Album_ID)
);

-- Create Album_Genre table
CREATE TABLE Album_Genre (
    Album VARCHAR2(20),
    Album_Genre VARCHAR2(20),
    CONSTRAINT album_genre_pk PRIMARY KEY (Album, Album_Genre)
);

-- Create Playlist table
CREATE TABLE Playlist (
    Playlist_ID VARCHAR2(20),
    Number_of_Songs VARCHAR2(20),
    Title VARCHAR2(20),
    Created_By VARCHAR2(20),
    CONSTRAINT playlist_pk PRIMARY KEY (Playlist_ID)
);

-- Create Song_on_Playlist table
CREATE TABLE Song_on_Playlist (
    Song VARCHAR2(20),
    Playlist VARCHAR2(20),
    Date_Added VARCHAR2(20),
    CONSTRAINT song_on_playlist_pk PRIMARY KEY (Song)
);

-- Create Artist_on_Playlist table
CREATE TABLE Artist_on_Playlist (
    Artist VARCHAR2(20),
    Playlist VARCHAR2(20),
    Date_Added VARCHAR2(20),
    CONSTRAINT artist_on_playlist_pk PRIMARY KEY (Artist)
);

-- Create SUser table
CREATE TABLE SUser (
    Username VARCHAR2(20),
    Age VARCHAR2(20),
    Country VARCHAR2(20),
    Email VARCHAR2(20),
    CONSTRAINT suser_pk PRIMARY KEY (Username)
);

-- Add foreign key constraints
ALTER TABLE Artist_Concert ADD CONSTRAINT artist_concert_fk FOREIGN KEY (Artist) REFERENCES Artist (Artist_ID);
ALTER TABLE Song ADD CONSTRAINT song_fk FOREIGN KEY (Artist) REFERENCES Artist (Artist_ID);
ALTER TABLE Song ADD CONSTRAINT song_fk2 FOREIGN KEY (Album) REFERENCES Album (Album_ID);
ALTER TABLE Song_Genre ADD CONSTRAINT song_genre_fk FOREIGN KEY (Song) REFERENCES Song (Song_ID);
ALTER TABLE Music_Video ADD CONSTRAINT music_video_fk FOREIGN KEY (Song) REFERENCES Song (Song_ID);
ALTER TABLE Album ADD CONSTRAINT album_fk FOREIGN KEY (Artist) REFERENCES Artist (Artist_ID);
ALTER TABLE Album_Genre ADD CONSTRAINT album_genre_fk FOREIGN KEY (Album) REFERENCES Album (Album_ID);
ALTER TABLE Song_on_Playlist ADD CONSTRAINT song_on_playlist_fk FOREIGN KEY (Song) REFERENCES Song (Song_ID);
ALTER TABLE Song_on_Playlist ADD CONSTRAINT song_on_playlist_fk2 FOREIGN KEY (Playlist) REFERENCES Playlist (Playlist_ID);
ALTER TABLE Artist_on_Playlist ADD CONSTRAINT artist_on_playlist_fk FOREIGN KEY (Artist) REFERENCES Artist (Artist_ID);
ALTER TABLE Artist_on_Playlist ADD CONSTRAINT artist_on_playlist_fk2 FOREIGN KEY (Playlist) REFERENCES Playlist (Playlist_ID);
ALTER TABLE Playlist ADD CONSTRAINT playlist_fk FOREIGN KEY (Created_By) REFERENCES
