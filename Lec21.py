def is_palindrome(string):
    if string == "":
        return True
    return string[0] == string[-1] and is_palindrome(string[1: -1])


print(is_palindrome("noon"))


def is_target_in_nested_list(target, nested_list):
    print("nested list:", nested_list)
    if type(nested_list) is int:
        return target == nested_list

    for element in nested_list:
        if is_target_in_nested_list(target, element):
            return True
    return False


print(is_target_in_nested_list(7, [1, 2, 4, [5, [6], 9]]))


def biggest_multiple_of_five(nested_list):
    # base case
    if type(nested_list) is int:
        if nested_list % 5 == 0:
            return nested_list
        else:
            return None
    # recursive step
    biggest = None
    for element in nested_list:
        best_answer = biggest_multiple_of_five(element)
        if best_answer is not None and (biggest is None or best_answer > biggest):
            biggest = best_answer
    return biggest


print(biggest_multiple_of_five([1, 5, 4, [1, [3], 5]]))
