SELECT u.username
FROM users u
JOIN (
  SELECT to_user_id, COUNT(*) as message_count
  FROM messages
  GROUP BY to_user_id
) as msg_count ON u.id = msg_count.to_user_id
ORDER BY msg_count.message_count DESC, u.username
LIMIT 1;
