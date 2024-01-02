SELECT username
FROM users
WHERE last_login_date >= '2024-01-01'
INDEXED BY search_users_by_last_login;
