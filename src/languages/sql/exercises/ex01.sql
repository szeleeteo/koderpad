CREATE TABLE orders (
    order_id INT NOT NULL,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price_per_unit FLOAT NOT NULL,
    order_status VARCHAR(50) NOT NULL
);

INSERT INTO orders (order_id, customer_id, order_date, product_name, quantity, price_per_unit, order_status) VALUES
(101, 1, '2023-01-10', 'Laptop', 2, 1000.00, 'Completed'),
(102, 2, '2023-01-15', 'Smartphone', 2, 500.00, 'Completed'),
(103, 1, '2023-02-10', 'Tablet', 1, 300.00, 'Completed'),
(104, 3, '2023-03-05', 'Headphones', 3, 100.00, 'Completed'),
(105, 2, '2023-03-12', 'Smartwatch', 1, 200.00, 'Completed'),
(106, 4, '2024-01-01', 'Laptop', 1, 950.00, 'Failed'),
(107, 1, '2024-01-07', 'Laptop', 1, 1000.00, 'Completed'),
(108, 4, '2024-04-15', 'Smartphone', 2, 450.00, 'Failed'),
(109, 1, '2024-05-10', 'Tablet', 1, 350.00, 'Completed'),
(109, 1, '2024-03-22', 'Headphones', 1, 350.00, 'Failed');


-- Question 1: Write a query to find the year and month with the highest total sales
-- Consider the available columns and state your assumptions
-- Hint: You can use to_char(), date_trunc() or extract() function to extract the month from the order_date column.






-- Question 2: Write a query to identify customers who have made multiple 'Completed' orders for the same product.





