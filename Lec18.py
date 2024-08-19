# Practice Problem #

from random import randint


def repeated_values(a_dict):
    for key_1 in a_dict:
        for key_2 in a_dict:
            if a_dict[key_1] == a_dict[key_2] and key_1 != key_2:
                return True
    return False


print(repeated_values({1: 2, 3: 6, 4: 6}))


def create_friend_dict():
    friend_list = ["sarah", "kamo", "shannon", "elishka", "amie", "jane", "brynn", "katherine"]
    friend_dict = {}
    for name in friend_list:
        friend_dict[name] = randint(-20, 20)
    return friend_dict


def find_best_friend(dictionary_of_friends):
    best_friend = None
    for key, value in dictionary_of_friends.items():
        if best_friend is None or value > dictionary_of_friends[best_friend]:
            best_friend = key
    return best_friend


print("Congrats,", find_best_friend(create_friend_dict()), "is your best friend!")


def is_shannon_in_this_room(things_in_room):
    count = 0
    for word in things_in_room:
        for letter in word:
            if letter == "s" or letter == "h" or letter == "a" or letter == "n" or letter == "o":
                count += 1
    if count >= 7:
        return True
    else:
        return False


things = ["kombucha", "aquafor"]
print(is_shannon_in_this_room(things))


def binary_search(target, sorted_list):
    first_index = 0
    last_index = len(sorted_list) - 1
    while last_index >= first_index:
        middle_index = (last_index + first_index) // 2
        if sorted_list[middle_index] == target:
            return middle_index
        elif sorted_list[middle_index] < target:
            first_index = middle_index + 1
        else:
            last_index = middle_index - 1
    return None

# def binary_search(target_integer, numbers):
#     start_index = 0  # defines beginning of valid search area for list
#     stop_index = len(numbers) - 1  # finds last item in valid search area of list
#     while start_index <= stop_index:  # if stop index crosses start index, we know the number is not in the list
#         middle_index = (start_index + stop_index) // 2  # defines search index at valid middle integer index
#         if numbers[middle_index] == target_integer:
#             return True
#         elif numbers[middle_index] < target_integer:  # cuts search area in half to the left or right of current index
#             start_index = middle_index + 1
#         else:
#             stop_index = middle_index - 1
#     return False


print(binary_search(0, [-10, -5, 3, 4, 5, 6, 7, 8, 13, 16, 18, 23]))
