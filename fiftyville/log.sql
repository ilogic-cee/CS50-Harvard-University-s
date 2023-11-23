-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports
WHERE street = 'Humphrey Street';
--Bakery withnesses--
SELECT * FROM interviews
WHERE transcript LIKE '%bakery%';
--witness 1 ruth--
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25;
--check against license plates--
SELECT p.name, bsl.activity, bsl.license_plate, bsl.year, bsl.month, bsl.day, bsl.hour, bsl.minute
FROM bakery_security_logs bsl
JOIN people p ON p.license_plate = bsl.license_plate
WHERE bsl.year = 2021 AND bsl.month = 7 AND bsl.day = 28 AND bsl.hour = 10 AND bsl.minute BETWEEN 15 AND 25;
--check witness 2 regards the atm--
SELECT * FROM atm_transactions
WHERE atm_location = 'Leggett Street'
AND year = 2021 AND month = 7 AND day = 28;
--add name of withdraws from atm--
SELECT a.*, p.name
FROM atm_transactions a
JOIN bank_accounts b ON a.account_number = b.account_number
JOIN people p ON b.person_id = p.id
WHERE a.atm_location 
