SELECT DATETIME(sent_at, '+30 seconds') AS expiry_time
FROM messages
WHERE id = 151;
