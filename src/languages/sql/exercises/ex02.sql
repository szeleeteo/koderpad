CREATE TABLE flights (
    flight_id INT NOT NULL,
    airline_id INT NOT NULL,
    departure_time TIMESTAMP NOT NULL,
    arrival_time TIMESTAMP NOT NULL,
    status VARCHAR(50) NOT NULL
);

CREATE TABLE airlines (
    airline_id INT NOT NULL,
    airline_name VARCHAR(100) NOT NULL
);

INSERT INTO flights (flight_id, airline_id, departure_time, arrival_time, status) VALUES
(1, 1, '2024-01-10 08:00:00', '2024-01-10 12:00:00', 'On-Time'),
(2, 2, '2024-01-15 09:30:00', '2024-01-15 13:30:00', 'Delayed'),
(3, 1, '2024-02-20 14:00:00', '2024-02-20 18:00:00', 'On-Time'),
(4, 3, '2024-03-05 06:00:00', '2024-03-05 10:30:00', 'Cancelled'),
(5, 2, '2024-03-12 20:00:00', '2024-03-13 00:30:00', 'On-Time');

INSERT INTO airlines (airline_id, airline_name) VALUES
(1, 'Airline A'),
(2, 'Airline B'),
(3, 'Airline C');



-- Question 1: Write a query to calculate the average flight duration for each airline.





-- Question 2: Write a query to find all flights that were either 'Delayed' or 'Cancelled.'





