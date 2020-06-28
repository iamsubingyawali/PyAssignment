input_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Implementing Bubble sort
for _ in range(0, len(input_list)):
    for j in range(0, len(input_list)-1):
        if input_list[j][1] > input_list[j+1][1]:
            input_list[j], input_list[j+1] = input_list[j+1], input_list[j]

print(input_list)
