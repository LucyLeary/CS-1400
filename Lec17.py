def string_to_id(strings):
    ids = []
    for string in strings:
        string_list = string.split(" ")
        ids += string_list[2]
    return ids


print(string_to_id(["Lindley Melvin 3", "Jackson Jensen 5", "Sally Mae 7"]))


def count_ones(strings):
    number_of_ones = 0
    for string in strings:
        for character in string:
            if character == "1":
                number_of_ones += 1
    return number_of_ones


def main():
    file = open(example.txt)
    lines = file.readlines()
    print(count_ones(lines))


if __name__ == "__main__":
    main()
