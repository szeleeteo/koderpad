CREATE TABLE students (
    student_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    grade INT NOT NULL,
    major VARCHAR(100) NOT NULL
);

CREATE TABLE courses (
    course_id INT NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    major VARCHAR(100) NOT NULL
);

INSERT INTO students (student_id, name, grade, major) VALUES
(1, 'John', 90, 'Computer Science'),
(2, 'Alice', 85, 'Mathematics'),
(3, 'Bob', 78, 'Computer Science'),
(4, 'Diana', 88, 'Physics'),
(5, 'Eve', 92, 'Mathematics');

INSERT INTO courses (course_id, course_name, major) VALUES
(1, 'Algorithms', 'Computer Science'),
(2, 'Calculus', 'Mathematics'),
(3, 'Quantum Physics', 'Physics'),
(4, 'Data Structures', 'Computer Science');



-- Question 1: Write a query to find the top-performing student in each major.





-- Question 2: Write a query to list all courses available for students in 'Mathematics'.





