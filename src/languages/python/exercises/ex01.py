"""
You are given a list of students data, where each student has a name, age and a list of grades.

Write a Python function that accepts the list and returns new list with the following criteria:

- Include only students who are 18 or older.
- Include a new key "average_grade" that contains the average of their grades.
- Exclude the original "age" and "grades" key from the output.
"""

students = [
    {"name": "Alice", "age": 17, "grades": [88, 92, 95]},
    {"name": "Bob", "age": 20, "grades": [75, 85, 90]},
    {"name": "Charlie", "age": 18, "grades": [80, 85, 90]},
    {"name": "Diana", "age": 22, "grades": [85, 88, 90]},
]
