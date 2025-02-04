CREATE TABLE employees (
    employee_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    department_id INT NOT NULL,
    hire_date DATE NOT NULL,
    salary FLOAT NOT NULL
);

CREATE TABLE departments (
    department_id INT NOT NULL,
    department_name VARCHAR(100) NOT NULL
);

INSERT INTO employees (employee_id, name, department_id, hire_date, salary) VALUES
(1, 'Alice', 101, '2020-06-15', 70000),
(2, 'Bob', 102, '2019-04-20', 80000),
(3, 'Charlie', 101, '2021-11-01', 60000),
(4, 'Diana', 103, '2018-07-12', 90000),
(5, 'Eve', 102, '2022-01-25', 75000);

INSERT INTO departments (department_id, department_name) VALUES
(101, 'Engineering'),
(102, 'Marketing'),
(103, 'HR');



-- Question 1: Write a query to find the average salary for each department.





-- Question 2: Write a query to list all employees hired after January 1, 2021.





