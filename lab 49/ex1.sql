CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER,
    registration_date DATE DEFAULT CURRENT_DATE
);

INSERT INTO users (name, email, age) VALUES
('Alice Johnson', 'alice@example.com', 28),
('Bob Smith', 'bob@example.com', 32),
('Charlie Brown', 'charlie@example.com', 25);

SELECT * FROM users;