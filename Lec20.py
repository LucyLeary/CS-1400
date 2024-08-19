def sum_numbers(numbers):
    if len(numbers) == 0:
        return 0
    sum = numbers[0] + sum_numbers(numbers[1:])
    return sum


print(sum_numbers([1, 2, 3]))

# Recursion is when a function calls itself
# Recursive Factorial:


def factorial(n):
    product = 1
    for factor in range(1, n + 1):
        product *= factor
    return factor


def recursive_factorial(n):
    if n <= 1:
        return 1
    factorial = n * recursive_factorial(n-1)
    return factorial


print(recursive_factorial(4))


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fibo = fibonacci(n - 2) + fibonacci(n - 1)
    return fibo


print(fibonacci(7))


def reverse_list(numbers):
    if len(numbers) == 0:
        return numbers
    return [numbers[-1]] + reverse_list(numbers[:-1])


print(reverse_list([1, 2, 3, 4, 5]))


import turtle


def tree(branch_length, turtle):
    if branch_length < 10:
        return
    turtle.forward(branch_length)
    turtle.right(30)
    tree(branch_length / 1.5, turtle)
    turtle.left(60)
    tree(branch_length / 1.5, turtle)
    turtle.right(30)
    turtle.forward(- branch_length)



def main():
    tree_turtle = turtle.Turtle()
    tree_turtle.speed(0)
    my_win = turtle.Screen()
    
