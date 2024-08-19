

def deepest_nest(nested_list):
    if type(nested_list) is not list:
        return 0
    depth = 0
    for item in nested_list:
        item_depth = 1 + deepest_nest(item)
        if item_depth > depth:
            depth = item_depth
    return depth


def deepest(nested_list):
    if type(nested_list) is not list:
        return 0
    depth = 0
    for item in nested_list:
        local_depth = 1 + deepest(item)
        if local_depth > depth:
            depth = local_depth
    return depth


def search(nested, target):
    if type(nested) is not list:
        return target == nested
    for item in nested:
        if search(item, target):
            return True
    return False


def flatten(nested):
    if type(nested) is not list:
        return [nested]
    flat_list = []
    for item in nested:
        flat_list += flatten(item)
    return flat_list


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


for n in [0, 1, 2, 3, 4, 5, 6]:
    print(fibonacci(n))


def check_consecutive(numbers):
    for index in range(len(numbers) - 1):
        if numbers[index] == numbers[index + 1]:
            return True
    return False


print(check_consecutive([1, 2, 3, 4, 5, 6, 7, 5, 8]))