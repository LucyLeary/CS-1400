simple_list = ["hello", 5, 5.7]
print(simple_list[-1])
print(simple_list[len(simple_list) - 1])
print(simple_list[-len(simple_list)])

simple_list += [1, 2, 3]
simple_list[0] = "goodbye"
simple_list.append(5)
print(simple_list)

for item in simple_list:
    print(item)

for index in range(len(simple_list)):
    print(simple_list[index])

even_numbers = [2, 4, 6, 8, 10]
new_numbers = []
for number in even_numbers:
    number += 1
    new_numbers += [number]
print(new_numbers)

for index in range(len(even_numbers)):
    even_numbers[index] += 1

print(even_numbers)


def letter_list(word):
    character_list = []
    for character in word:
        character_list += character
    return character_list


print(letter_list("lucy"))

example_list = [1, 2]
example_list.append([4])
print(example_list)
