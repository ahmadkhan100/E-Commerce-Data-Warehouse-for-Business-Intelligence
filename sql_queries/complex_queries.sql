-- complex_queries.sql

-- Query to get total sales per product category
SELECT category, SUM(price * quantity) AS total_sales
FROM ecommerce.products p
JOIN ecommerce.order_items oi ON p.product_id = oi.product_id
GROUP BY category;

-- Query to detect anomalies in order amounts
SELECT order_id, total_amount, SUM(price * quantity) AS calculated_amount
FROM ecommerce.orders o
JOIN ecommerce.order_items oi ON o.order_id = oi.order_id
GROUP BY order_id, total_amount
HAVING total_amount <> SUM(price * quantity);
