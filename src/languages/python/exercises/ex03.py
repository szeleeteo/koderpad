def double_and_append_to_list(element, elements=[]):
    """This function takes an element and appends its double to a list."""
    elements.append(element * 2)
    return elements


# what is the output of print statement?
first_list = double_and_append_to_list(3, [2, 4])
# print(first_list)

# what is the output of print statement?
second_list = double_and_append_to_list(12)
# print(second_list)

# what is the output of print statement?
third_list = double_and_append_to_list(100)
# print(third_list)
