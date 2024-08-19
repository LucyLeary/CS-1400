def sum_nested_list(numbers):
    if len(numbers) == 0:
        return 0
    elif type(numbers[0]) is int:
        return numbers[0] + sum_nested_list(numbers[1:])
    elif type(numbers[0]) is list:
        return sum_nested_list(numbers[0]) + sum_nested_list(numbers[1:])


print(sum_nested_list([1, [1, 2, 12, [1, 2]]]))

# example from Kellen


def sum_nested(item):
    if type(item) is not list:
        return item
    my_sum = 0
    for number in item:
        my_sum += sum_nested(number)
    return my_sum


print(sum_nested([1, 2, 4, [1, 2]]))
