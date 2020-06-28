def check_in_range(input_range, num):
    if int(num) in range(int(input_range[0]), int(input_range[1])):
        return True
    else:
        return False


num_range = input("Enter Number range(eg. 4-10): ")
number = input("Enter the number: ")
range_list = (num_range.split("-"))
print(check_in_range(range_list, number))
