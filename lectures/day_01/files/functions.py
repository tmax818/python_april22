## functions.py
## demo

def add(param1, param2): # define a function
    print( param1 + param2 ) # prints the  param1 and param2 to the terminal
    return param1 + param2 

def divide(a,b):
    print(a / b, a % b)
    return a/b, a % b

print(add(3,4))
print(divide(10,2))
print(divide(b = 2, a = 10))

def greet(name="Python Programmer"):
    print(f"Hello, {name}")

greet("Arthur")
greet()

# def divide(numerator, denominator = 1):
#     return numerator/denominator

# print(divide(10))
# print(divide(denominator = 2, numerator = 10))



# # TODO function invocation

# # TODO function_name('argument')

# ## TODO returning values



# # def number_of_military_branches():
# #     return 5
# # print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# #3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())

# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

