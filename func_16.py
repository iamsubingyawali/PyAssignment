square = lambda number: number ** 2
cube = lambda number: number ** 3

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(map(square, my_list)))
print(list(map(cube, my_list)))
