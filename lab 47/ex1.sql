CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER,
    registration_date DATE DEFAULT CURRENT_DATE
);

INSERT INTO users (name, email,) VALUES ('Alice Johnson', 'alice@example.com', 28),


SELECT * FROM users;

