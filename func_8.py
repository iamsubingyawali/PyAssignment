def make_unique(input_list):
    input_set = set(input_list)
    list_out = list(input_set)
    return list_out


my_list = [1, 2, 3, 3, 3, 3, 4, 5]
print(make_unique(my_list))
