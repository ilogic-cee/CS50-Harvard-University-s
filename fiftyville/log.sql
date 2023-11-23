-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports
WHERE street = 'Humphrey Street';
--Bakery withnesses--
SELECT * FROM interviews
WHERE transcript LIKE '%bakery%';

