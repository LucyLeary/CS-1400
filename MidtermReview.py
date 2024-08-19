# difference between parameters and arguments, arguments are what you pass into parameters
# study from assignments

def other_function(val1, val2):
    print(val1 + val2)


def function(num1, num2):  # parameters here
    other_function(num1, num2)  # arguments here
    return num1 + num2


function(2, 3)  # arguments here


def fraction(numerator, denominator):
    return str(numerator) + "/" + str(denominator)


print(fraction(3, 4))


def return_longer(string1, string2):
    if len(string1) > len(string2):
        return string1
    else:
        return string2


print(return_longer("hello old pal", "my friend"))


# def remove_spaces(phrase):
#     new_phrase = ""
#     for index in range(len(phrase)):
#         if phrase[index] != " ":
#             new_phrase += phrase[index]
#     return new_phrase

def remove_spaces(phrase):
    result = ""
    for character in phrase:
        if character != " ":
            result = result + character
    return result


print(remove_spaces("I like to go to school."))


def remove_fives(num_list):
    new_list = []
    for item in num_list:
        if item != 5:
            new_list.append(item)
    return new_list


print(remove_fives([1, 3, 5, 7, 5, 7, 5, 7]))

# LECTURE 10 REVIEW:
a_list = [1, 2, 3]
print(a_list[0:])  # slice produces a new list, index produces a number by itself
print(a_list[0])

# MIDTERM 2 REVIEW #

# can take a decimal number, divide it by 2 and take the remainder, remainders backwards will be binary
# strings are immutable
string = ".!   hi yo   !!"
string.strip()  # does nothing
new_string = string.strip(".!")
new_string = new_string.strip()
print(new_string)
string_list = string.split()
print(string_list)
string_list = new_string.split()
print(string_list)

# ONLY use is for None, OR to test if two things refer to the same object

# objects are assigned to variables
x = 5  # x --> 5
y = x  # y --> 5
print(x is y)
print(x == y)  # false

x = 5  # x --> 5
y = 5  # y --> different 5
print(x == y)
print(x is y)  # false

x = None
print(x is None)

# look at lecture 18, practice scope and object stuff
# strings are special, immutable, if you pass it through a function it will not change


def count_strings(strings):
    dict = {}
    for word in strings:
        count = dict.get(word, 0)
        dict[word] = count + 1
    return dict
