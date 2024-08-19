def double_number(number):
    return number * 2


for loop in range(1, 11):
    doubled_number = double_number(loop)
    print(doubled_number)


# # Lecture goals:
# - Learn how to structure programs with multiple functions
# - import() sometimes gives you extra output, runs all the code in the imported file
# - write leftover non-function code inside main() function
def main():
    pass


if __name__ == "__main()__":
    main()

# Do not have any program code outside function.
# Use main function to show when program starts to run.


def double_number(user_number):
    return user_number * 2


def main():
    user_number = float((input("give me a number ")))  # Make sure input() stays in main() function, not in function() function.
    doubled_number = double_number(user_number)
    print(doubled_number)


if __name__ == "__main__":
    main()


# if something():
#   do something
# else:
#   do something else
# boolean
# 10 == 12 # is an equality operator/logical expression (is it true or false?)
# != means NOT equal, <= less than or equal, >= greater than or equal to
# always either true or false

age = int(input("How old are you? "))
if age < 12:
    print("it's a baby")
else:
    print("it's time")


