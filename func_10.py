def return_even(input_list):
    new_list = []
    for item in input_list:
        if item % 2 == 0:
            new_list.append(item)
    return new_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(return_even(my_list))
