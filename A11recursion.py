"""
Initial code written by David Johnson, University of Utah.
This, and all derived works may not be publicly shared.

Assignment completed by Lyndsey Schindler and Lucy Leary.
"""


def flatten_list(nested_list):
    """
    This function takes in a nested list and returns a list without nesting.
    :param nested_list: A single integer, a list of integers, or a nested list.
    :return: A list with all the same values as the parameter list, but without any nesting.
    """

    if type(nested_list) is not list:
        return [nested_list]
    flattened_list = []
    for number in nested_list:
        flattened_list += flatten_list(number)
    return flattened_list


def length_of_longest_string(nested_strings):
    """
    Runs through all the strings in the parameter and returns the length of the longest string.
    :param nested_strings: A nested list of strings or a single string.
    :return: An integer value representing the length of the longest string in the list.
    """

    if type(nested_strings) is str:
        return len(nested_strings)
    longest = 0
    for item in nested_strings:
        best_from_item = length_of_longest_string(item)
        if longest < best_from_item:
            longest = best_from_item
    return longest


def main():
    print("Testing flatten_list([[1, 2], 3, 5]). Expecting a result of [1, 2, 3, 5]. Computed",
          flatten_list([[1, 2], 3, 5]))
    print("Testing flatten_list([]). Expecting a result of []. Computed",
          flatten_list([]))
    print("Testing flatten_list(10). Expecting a result of [10]. Computed",
          flatten_list(10))
    print("Testing flatten_list([[1, [2]], 3, 5]). Expecting a result of [1, 2, 3, 5]. Computed",
          flatten_list([[1, [2]], 3, 5]))
    print("Testing flatten_list([100]). Expecting a result of [100]. Computed",
          flatten_list([100]))
    print("Testing flatten_list([100, 200]). Expecting a result of [100, 200]. Computed",
          flatten_list([100, 200]))
    print()

    print("Testing length_of_longest_string([]). Expecting a result of 0. Computed",
          length_of_longest_string([]))
    print("Testing length_of_longest_string('apple'). Expecting a result of 5. Computed",
          length_of_longest_string('apple'))
    print("Testing length_of_longest_string(['help', ['we', 'need', 'help'], 'please']). "
          "Expecting a result of 6. Computed", length_of_longest_string(['help', ['we', 'need', 'help'], 'please']))
    print("Testing length_of_longest_string(['sunshine']). Expecting a result of 8. Computed",
          length_of_longest_string(['sunshine']))
    print("Testing length_of_longest_string(['sunshine', 'slippers', 'taco', 'banana']). Expecting a result of 8. "
          "Computed", length_of_longest_string(['sunshine', 'slippers', 'taco', 'banana']))
    print("Testing length_of_longest_string(['telephone', ['we', 'need', 'help'], 'please']). Expecting a result of 9. "
          "Computed", length_of_longest_string(['telephone', ['we', 'need', 'help'], 'please']))


if __name__ == "__main__":
    main()
