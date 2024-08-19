number = 5
other_number = 7
number >= 0 and number <= 10 and other_number > 0 and number > other_number

def absolute_value(new_number):
    if new_number <= 0:
        return new_number * -1
    else:
        return new_number

print(absolute_value(7))