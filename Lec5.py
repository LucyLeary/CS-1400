# Warmup Exercise: #
def f(x):
    print(x**2 + 5)


f(5)
f(10)

# Make sure to use float() and int() at correct times. Ask if you want a decimal. #
# Watch for line width and color, comments, and drawing at current location.

# Return Statement returns value to function call


def return_one():
    return 1


old_value = 5
plus_one = old_value + return_one()
print(plus_one)

def sum_2_numbers(number1, number2):
    summer = number1 + number2
    return summer


the_sum = sum_2_numbers(10, 20)
print(the_sum)

def count():
    for number in range(10):
        return number
print(count())

# Only prints 0, when python sees return statement, it leaves the function.
# Return ENDS the function. It is only used for computations, not Turtle() commands.



