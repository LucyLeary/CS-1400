# Assignment 8 created by Anonymous
from timeit import default_timer
from random import randrange, shuffle


# curves all numbers in a list so the highest number is 100
def curve_scores(integers):
    biggest_value = None
    for integer in integers:
        if integer >= 0 and (biggest_value == None or integer > biggest_value):
            biggest_value = integer  # uses sequential search to find largest value in list
    if biggest_value == None:
        return integers
    else:
        curve_value = 100 - biggest_value  # finds the value the numbers need to be curved by
        new_list = []  # creates an accumulation loop for curved numbers
        for integer in integers:
            new_list.append(curve_value + integer)
        return new_list


# checks if a list of strings contains any duplicate strings
def contains_duplicate(strings):
    for index_1 in range(len(strings)):  # uses nested loop to check whether 2 different indices hold equivalent values
        for index_2 in range(index_1 + 1, len(strings)):
            if strings[index_1] == strings[index_2]:
                return True
    return False


# converts a list to a string
def list_to_string(integers):
    if len(integers) == 0:  # check if the list is empty because code only works for lists with length >= 1
        return "[]"
    else:
        string = "["
        for index in range(len(integers) - 1):  # converts all but last integer to a string and adds a comma and space
            string += str(integers[index])
            string += ", "
        string += str(integers[-1])  # converts last integer in list to a string
        string += "]"
        return string


# finds the smallest positive multiple of three in a list of numbers
def find_smallest_positive_multiple_of_three(integers):
    smallest_multiple = None
    for integer in integers:  # loops through list to check whether a number is a multiple of 3 and smallest so far
        if integer % 3 == 0 and integer > 0 and (smallest_multiple == None or integer < smallest_multiple):
            smallest_multiple = integer
    return smallest_multiple


# finds whether a target number is contained in a list using sequential search
def sequential_search(target_integer, numbers):
    for number in numbers:
        if target_integer == number:
            return True
    return False


# faster method for finding whether a target value is contained in a pre-sorted list
def binary_search(target_integer, numbers):
    start_index = 0  # defines beginning of valid search area for list
    stop_index = len(numbers) - 1  # finds last item in valid search area of list
    while start_index <= stop_index:  # if stop index crosses start index, we know the number is not in the list
        middle_index = (start_index + stop_index) // 2  # defines search index at valid middle integer index
        if numbers[middle_index] == target_integer:
            return True
        elif numbers[middle_index] < target_integer:  # cuts search area in half to the left or right of current index
            start_index = middle_index + 1
        else:
            stop_index = middle_index - 1
    return False


# measures how long it takes to search for 50 items in different list sizes using sequential and binary search methods
def measure_search_times():
    for list_size in [10000, 100000, 1000000, 10000000]:
        my_list = list(range(list_size))  # creates lists of size list_size
        shuffle(my_list)  # puts list items into a random order
        start = default_timer()  # checks time before search begins
        for count in range(50):  # finds 50 random target values and searches for them using sequential search
            random_value = randrange(list_size)
            sequential_search(random_value, my_list)
        stop = default_timer()  # checks time after search ends
        average_time_sequential = (stop - start) / 50  # uses start and stop times to find average time for one search
        start = default_timer()  # finds start time for binary search
        my_list.sort()  # sorts the shuffled list so that binary search can be used
        for count in range(50):  # finds 50 random target values and searches for them in list
            random_value = randrange(list_size)
            binary_search(random_value, my_list)
        stop = default_timer()  # finds stop time
        average_time_binary = (stop - start) / 50  # finds average time for binary search including sort time
        print("For size", list_size, 'average elapsed time for sequential search is', f'{average_time_sequential:.8f}',
              'and average elapsed time for binary search is', f'{average_time_binary:.8f}')  # reports average times


def main():
    # testing the curve_scores function
    print("Testing the curve_scores function")
    print("Testing curve_scores([45, 85, 90]). Expecting a result of [55, 95, 100] and computed a result of",
          curve_scores([45, 85, 90]))
    print("Testing curve_scores([]). Expecting a result of [] and computed a result of",
          curve_scores([]))
    print("Testing curve_scores([0, 0, 0, 0]). Expecting a result of [100, 100, 100, 100] and computed a result of",
          curve_scores([0, 0, 0, 0]))
    print("Testing curve_scores([10, 100]). Expecting a result of [10, 100] and computed a result of",
          curve_scores([10, 100]))
    print()

    # testing the contains_duplicate function
    print("Testing the contains_duplicate function")
    print("""Testing contains_duplicate(["hi", "bye"]). Expecting a result of False and computed a result of""",
          contains_duplicate(["hi", "bye"]))
    print("Testing contains_duplicate([]). Expecting a result of False and computed a result of",
          contains_duplicate([]))
    print("""Testing contains_duplicate(["the", "boy", "the"]). Expecting a result of True and computed a result of""",
          contains_duplicate(["the", "boy", "the"]))

    # testing the list_to_string function
    print("Testing the list_to_string function")
    print("""Testing list_to_string([1, 2, 3]). Expecting a result of "[1, 2, 3]" and computed a result of""",
          list_to_string([1, 2, 3]))
    print("""Testing list_to_string([]). Expecting a result of "[]" and computed a result of""",
          list_to_string([]))
    print("""Testing list_to_string([-1]). Expecting a result of "[-1]" and computed a result of""",
          list_to_string([-1]))

    # testing the find_smallest_positive_multiple_of_three function
    print("Testing the find_smallest_positive_multiple_of_three function")
    print("Testing find_smallest_positive_multiple_of_three([-3, 0, 2, 3, 1, 6]). Expecting a result of 3 and computed " 
          "a result of", find_smallest_positive_multiple_of_three([-3, 0, 2, 3, 1, 6]))
    print("Testing find_smallest_positive_multiple_of_three([]). Expecting a result of None and computed a result of",
          find_smallest_positive_multiple_of_three([]))

    # testing the sequential_search function
    print("Testing the sequential_search function")
    print("Testing sequential_search(10, [2, 5, 10, 20]). Expecting a result of True and computed "
          "a result of", sequential_search(10, [2, 5, 10, 20]))
    print("Testing sequential_search(-1, []). Expecting a result of False and computed "
          "a result of", sequential_search(-1, []))

    # testing the binary_search function
    print("Testing the binary_search function")
    print("Testing binary_search(10, [2, 5, 10, 20]). Expecting a result of True and computed "
          "a result of", binary_search(10, [2, 5, 10, 20]))
    print("Testing binary_search(-1, []). Expecting a result of False and computed "
          "a result of", binary_search(-1, []))

    # informally testing measure_search_times function
    measure_search_times()


if __name__ == "__main__":
    main()


# For sequential search, each time the list increased 10 times in size, the time it took to search the list increased
# by about a factor of 10.
# For the unsorted binary search, as the list size increased, the time it took to search the list only increased by
# about .0000015 seconds each time.

# After taking into account the time it takes to sort an unsorted list, binary search takes much longer to run.
# Binary search was slower than sequential search in every case, and the time it took to run increased by a power of
# 10 each time the list size increased by a power of 10.

# After repeating the binary and sequential searches 50 times each instead of 10 times each, the average time for the
# binary search decreased in comparison to the sequential search. I think this is because we only had to sort the list
# once, so the added time from sorting the list had a smaller impact on the average time per binary search when we ran
# many binary searches on the same list.
# Sequential search is appropriate to use for smaller list sizes and for unsorted lists. Binary search should be used
# for sorted lists, and for unsorted lists if binary search needs to be used many different times on the same list.
