CREATE TABLE books (
    book_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    author_id INT NOT NULL,
    publication_year INT NOT NULL,
    price FLOAT NOT NULL
);

CREATE TABLE authors (
    author_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    nationality VARCHAR(100) NOT NULL
);

INSERT INTO books (book_id, title, author_id, publication_year, price) VALUES
(1, 'Book A', 1, 2010, 15.99),
(2, 'Book B', 2, 2015, 20.99),
(3, 'Book C', 1, 2020, 25.50),
(4, 'Book D', 3, 2018, 12.75),
(5, 'Book E', 2, 2022, 30.00);

INSERT INTO authors (author_id, name, nationality) VALUES
(1, 'Author 1', 'USA'),
(2, 'Author 2', 'UK'),
(3, 'Author 3', 'Canada');



-- Question 1: Write a query to find the author who has the most expensive book.





-- Question 2: Write a query to list all books published after 2015 along with their authors’ names.





