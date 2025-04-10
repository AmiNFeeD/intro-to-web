CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    stock_quantity INTEGER NOT NULL,
    discontinued BOOLEAN DEFAULT FALSE
);

INSERT INTO products (product_name, price, stock_quantity) VALUES
('Laptop', 999.99, 10),
('Smartphone', 599.99, 20),
('Headphones', 199.99, 15);

UPDATE products
SET price = 1099.99
WHERE product_name = 'Laptop';

UPDATE products
SET discontinued = TRUE
WHERE product_name = 'Headphones';

DELETE FROM products
WHERE discontinued = TRUE;

SELECT * FROM products;