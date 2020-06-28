sort_list = lambda input_list: sorted(input_list, key=lambda i: i['a'])

my_list = [{'a': 1}, {'a': 2}, {'a': 8}, {'a': 78}, {'a': 0}]
print(sort_list(my_list))
