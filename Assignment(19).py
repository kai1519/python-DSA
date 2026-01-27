# 1. Function to print “TasiNCoder”
def print_name():
    print("TasiNCoder")


# 2. Function which expects two arguments and prints them
def print_two_args(a, b):
    print(a)
    print(b)


# 3. Function which expects an unknown number of arguments
def unknown_args(*args):
    for i in args:
        print(i)


# 4. Function which expects keyword arguments
def keyword_args(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


# 5. Function which expects a list as an argument
def list_argument(lst):
    for item in lst:
        print(item)


# 6. Function to find maximum of four numbers
def max_of_four(a, b, c, d):
    return max(a, b, c, d)


# 7. Function to sum all numbers in a list
def sum_of_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


# 8. Function to multiply all numbers in a list
def multiply_of_list(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


# 9. Function to check whether a number falls in a given range
def check_range(num, start, end):
    return start <= num <= end


# 10. Function to check whether a number is even or odd
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
