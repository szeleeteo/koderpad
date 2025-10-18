"""
Study the code below. What will be the output of this code?
If the next two commented lines are uncommented, what will be the output?
Repeat for the last two commented lines.
"""


def double_and_append_to_list(element, elements=[]):
    """
    Double the value of an input.
    Append the new value to a list provided; if no list is provided, use a new empty list.
    Return the list.
    """
    elements.append(element * 2)
    return elements


first_list = double_and_append_to_list(3, [2, 4])
print(first_list)

# second_list = double_and_append_to_list(12)
# print(second_list)

# third_list = double_and_append_to_list("X")
# print(third_list)
