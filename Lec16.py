def add_number_to_even_keys(pairs, number):
    """
    Add change to the values associated with an even key
    :param pairs: A dictionary of integer keys and values
    :param number: A number to add to even-key values
    :return: The modified pairs dictionary
    """
    for key in pairs:
        if key % 2 == 0:
            pairs[key] += number
    return pairs


my_dictionary = {1: 3, 2: 4, 3: 9, 7: 8, 4: 5}
print(add_number_to_even_keys(my_dictionary, 7))


def make_city_state_pairs(cities, states):
    city_state_pairs = {}
    for index in range(len(cities)):
        city_state_pairs[cities[index]] = states[index]
    return city_state_pairs


list_1 = ['salt lake', 'denver', 'new york city', 'logan', 'LA']
list_2 = [1, 2, 3, 4, 5]
print(make_city_state_pairs(list_1, list_2))
