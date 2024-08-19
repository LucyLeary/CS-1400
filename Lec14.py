# Binary Search Guest Lecture
# Use a while loop because we don't know how many times we'll repeat loop

def binary_search(sorted_list, target_value):
    start_index = 0
    stop_index = len(sorted_list) - 1
    while start_index <= stop_index:
        middle_index = (start_index + stop_index)//2
        if sorted_list[middle_index] == target_value:
            return middle_index
        elif sorted_list[middle_index] < target_value:
            start_index = middle_index + 1
        else:
            stop_index = middle_index - 1
    return None

# can sort list with my_list.sort()
