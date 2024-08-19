# TIMER

from timeit import default_timer


def is_number_in_list(number_to_find, numbers):
    for number in numbers:
        if number == number_to_find:
            return True
    return False


def find_shortest_word(words):
    shortest_word = None
    for word in words:
        if len(word) > 0 and (shortest_word == None or len(word) < len(shortest_word)):
            shortest_word = word
    return shortest_word


def main():
    print('Testing is_number_in_list(5, [5, 3, 2, 8, -1]). Expect True and got',
          is_number_in_list(5, [5, 3, 2, 8, -1]))
    size = 10000
    big_list = list(range(size))
    start = default_timer()
    is_number_in_list(-1, big_list)
    stop = default_timer()
    print("For size", size, 'Elapsed time', stop - start)

    size = 10000000
    big_list = list(range(size))
    start = default_timer()
    is_number_in_list(-1, big_list)
    stop = default_timer()
    print("For size", size, 'Elapsed time', stop - start)

    print(find_shortest_word(["all", "never", "accounting", "baby", "it"]))


if __name__ == "__main__":
    main()
