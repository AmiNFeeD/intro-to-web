BEGIN;

INSERT INTO users (name, email, age) VALUES
('David Green', 'david@example.com', 40);

UPDATE users
SET age = 35
WHERE name = 'Alice Johnson';

DELETE FROM users
WHERE name = 'Charlie Brown';

ROLLBACK;

SELECT * FROM users;