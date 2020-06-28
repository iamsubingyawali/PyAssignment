def find_max(input_list):
    return max(input_list)


num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")
num_3 = input("Enter third number: ")

my_num = [num_1, num_2, num_3]

print("The max of three numbers is: ", find_max(my_num))
