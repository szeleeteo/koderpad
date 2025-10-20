def double_and_append_to_list(element, elements=[]):
    elements.append(element * 2)
    return elements


# what will be the output of print statement?
first_list = double_and_append_to_list(3, [2, 4])
print(first_list)

# what will be the output of print statement?
# second_list = double_and_append_to_list(12)
# print(second_list)

# what will be the output of print statement?
# third_list = double_and_append_to_list("G")
# print(third_list)
