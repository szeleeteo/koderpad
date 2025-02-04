CREATE TABLE sales (
    sale_id INT NOT NULL,
    store_id INT NOT NULL,
    product_id INT NOT NULL,
    sale_date DATE NOT NULL,
    amount FLOAT NOT NULL
);

CREATE TABLE stores (
    store_id INT NOT NULL,
    store_name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL
);

INSERT INTO sales (sale_id, store_id, product_id, sale_date, amount) VALUES
(1, 1, 101, '2023-01-10', 500.00),
(2, 2, 102, '2023-02-15', 300.00),
(3, 1, 103, '2023-03-20', 150.00),
(4, 3, 101, '2023-04-25', 450.00),
(5, 2, 104, '2023-05-30', 700.00);

INSERT INTO stores (store_id, store_name, location) VALUES
(1, 'Store A', 'New York'),
(2, 'Store B', 'San Francisco'),
(3, 'Store C', 'Chicago');



-- Question 1: Write a query to find the total sales amount for each store.





-- Question 2: Write a query to identify which store had the highest single sale.





