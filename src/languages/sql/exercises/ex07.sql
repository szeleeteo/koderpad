CREATE TABLE customers (
    customer_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    registration_date DATE NOT NULL
);

CREATE TABLE orders (
    order_id INT NOT NULL,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount FLOAT NOT NULL
);

CREATE TABLE payments (
    payment_id INT NOT NULL,
    order_id INT NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount FLOAT NOT NULL,
    payment_method VARCHAR(50) NOT NULL
);

INSERT INTO customers (customer_id, name, registration_date) VALUES
(1, 'Alice', '2022-01-01'),
(2, 'Bob', '2022-01-15'),
(3, 'Charlie', '2022-02-01'),
(4, 'Diana', '2022-03-10'),
(5, 'Eve', '2022-03-25');

INSERT INTO orders (order_id, customer_id, order_date, total_amount) VALUES
(101, 1, '2022-01-20', 500.00),
(102, 1, '2022-02-15', 300.00),
(103, 2, '2022-01-25', 700.00),
(104, 3, '2022-02-10', 200.00),
(105, 4, '2022-03-20', 1000.00),
(106, 5, '2022-03-30', 400.00);

INSERT INTO payments (payment_id, order_id, payment_date, payment_amount, payment_method) VALUES
(1, 101, '2022-01-21', 500.00, 'Credit Card'),
(2, 102, '2022-02-16', 200.00, 'Credit Card'),
(3, 103, '2022-01-26', 700.00, 'PayPal'),
(4, 104, '2022-02-11', 200.00, 'Credit Card'),
(5, 105, '2022-03-25', 800.00, 'Bank Transfer'),
(6, 105, '2022-03-28', 200.00, 'Credit Card'),
(7, 106, '2022-03-31', 400.00, 'PayPal');



-- Question 1: Find customers who have not fully paid for all their orders.
