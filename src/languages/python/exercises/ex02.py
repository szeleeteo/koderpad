"""
Given a list of student records, where each record contains a name, age, and a
list of grades, create a pandas dataframe containing only the students who are
at least 18 years old.
The dataframe should only include the student’s name and their average grade,
excluding all other columns.
"""

import pandas as pd

from languages.python.utils import print_dataframe

class_students = [
    {"name": "Alice", "age": 17, "grades": [88, 92, 95]},
    {"name": "Bob", "age": 20, "grades": [72, 86, 91]},
    {"name": "Charlie", "age": 18, "grades": [80, 85, 90]},
    {"name": "Diana", "age": 22, "grades": [85, 53, 90, 99]},
]

df = pd.DataFrame(class_students)

# write your code here

print_dataframe(df, title="Students DataFrame")
