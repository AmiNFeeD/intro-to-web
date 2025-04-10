CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    department TEXT,
    salary INTEGER,
    hire_date DATE
);

INSERT INTO employees (first_name, last_name, department, salary, hire_date) VALUES
('Alice', 'Johnson', 'IT', 60000, '2021-05-10'),
('Bob', 'Smith', 'Finance', 72000, '2018-03-15'),
('Charlie', 'Wilson', 'HR', 50000, '2020-08-22'),
('Daniel', 'Lee', 'IT', 65000, '2019-11-01'),
('Eve', 'Watson', 'Marketing', 58000, '2022-01-05');

SELECT * FROM employees;

SELECT first_name, salary FROM employees;

SELECT * FROM employees WHERE department = 'IT';