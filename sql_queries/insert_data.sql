-- insert_data.sql

-- Insert sample data into customers table
INSERT INTO ecommerce.customers (first_name, last_name, email) VALUES
('John', 'Doe', 'johndoe@example.com'),
('Jane', 'Smith', 'janesmith@example.com');

-- Insert sample data into products table
INSERT INTO ecommerce.products (product_name, category, price, stock_quantity) VALUES
('Laptop', 'Electronics', 999.99, 50),
('Smartphone', 'Electronics', 499.99, 200);

-- Insert sample data into orders table
INSERT INTO ecommerce.orders (customer_id, total_amount) VALUES
(1, 1499.98),
(2, 499.99);

-- Insert sample data into order_items table
INSERT INTO ecommerce.order_items (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 999.99),
(1, 2, 1, 499.99),
(2, 2, 1, 499.99);
