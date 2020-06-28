arr_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr_2 = [2, 4, 6, 8, 10]

intersection = lambda i: i in arr_1

print(list(filter(intersection, arr_2)))
