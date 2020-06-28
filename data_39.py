my_tuple = (1, 2, 3, 4, 5, 'a', 'b', 'c')
counter = 1
var_tuple = ()
for item in my_tuple:
    var_tuple += ("var_" + str(counter),)
    counter += 1

var_tuple = my_tuple

print(var_tuple[5])
