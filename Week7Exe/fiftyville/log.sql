-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Capture crime scene report
SELECT * FROM crime_scene_reports WHERE street = "Humphrey Street" AND day = 28 AND month = 7 AND year = 2021;

-- Gather information from interviews
SELECT name, transcript FROM interviews WHERE day = 28 AND month = 7 AND year = 2021 AND transcript LIKE "%bakery%";

-- Check the bakery security logs for suspects leaving the scene and cross license plates with people to find their ID
SELECT name, id FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2021 AND hour = 10 AND activity = "exit" AND minute < 25 AND minute > 15);

-- Suspects
-- Bruce 686048

-- Check the withdrawals from atm_transactions and find the ID's of those who made a withdrawal that morning before the robbery.
SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2021 AND atm_location = "Leggett Street" AND transaction_type = "withdraw");

-- Check the phone call logs
SELECT id FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60);

-- Check the flights the following morning
SELECT id FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE day = 29 AND month = 7 AND year = 2021 AND origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") ORDER BY hour, minute LIMIT 1));

-- The thief: Bruce 686048

-- Find out what city he escaped to
SELECT city FROM airports WHERE id IN (SELECT destination_airport_id FROM flights WHERE id IN (SELECT id FROM flights WHERE day = 29 AND month = 7 AND year = 2021 AND origin_airport_id IN (SELECT id FROM airports WHERE city = "Fiftyville") ORDER BY hour, minute LIMIT 1));

-- Find the accomplice
SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60 AND caller IN (SELECT phone_number FROM people WHERE id = 686048));