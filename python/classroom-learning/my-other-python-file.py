# -- ******************************************************************
# This is a file for showing people how to do a python file
# -- ******************************************************************

print("Hello World")

integer_var = 123   # -- Integer
float_var = 123.45  # -- Float
string_var = "Text" # -- String
bool_var = True     # -- Boolean

# -- ******************************************************************
# -- Variable Naming Standards
# -- ******************************************************************
# -- Separate variables by underscores or something like CamelCase
# -- No reserved words must be used - i.e. print = 10
# -- Variables are case sensititve so:
# --  age = 21
# --  Age = 32
# -- These will both have different results
# -- ******************************************************************

input_name = input("Please input your name: ")
input_animal = input("Please input your favourite animal: ")
print (input_name + "'s favourite animal is a " + input_animal)