# Assignment A4
# CS 1400
# Starter code by David Johnson
# Assignment completed by Lucy Leary and Lyndsey Schindler

# The multiply function computes the product of two factors with repeated adding.
def multiply(factor1, factor2):
    product = 0
    for counter in range(factor2):
        product += factor1
    return product


# The choose_larger function returns the larger of two parameters.
def choose_larger(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2


# The describe_number function returns the sign of a value.
def describe_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"


# The add_a_or_an_to_word function adds an article to a non-plural noun.
def add_a_or_an_to_word(word):
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        return "an " + word
    else:
        return "a " + word


# The add_a_or_an_or_any function adds article to both plural and non-plural nouns.
def add_a_or_an_or_any_to_word(text):
    if text[-1] == "s":
        return "any " + text
    else:
        return add_a_or_an_to_word(text)


# The collect_punctuation function creates a list of punctuation in a sentence.
def collect_punctuation(sentence):
    punctuation = ""
    for character in sentence:
        if character == ".":
            punctuation = punctuation + "."
        elif character == ",":
            punctuation = punctuation + ","
        elif character == "!":
            punctuation = punctuation + "!"
        elif character == "'":
            punctuation = punctuation + "'"
    return '"' + punctuation + '"'


# The translate_pirate_word function translates english words into pirate words
def translate_pirate_word(english_word):
    if english_word == "my":
        return "me"
    elif english_word == "you":
        return "ye"
    elif english_word == "is" or english_word == "are":
        return "be"
    elif english_word == "hello":
        return "ahoy"
    elif english_word == "yes":
        return "arr"
    elif english_word == "friend":
        return "matey"
    else:
        return english_word


# The translate_to_pirate function translates english sentences into pirate sentences
def translate_to_pirate(english_sentence):
    english_sentence += " "
    word = ""
    pirate_sentence = ""
    for character in english_sentence:
        if character != " ":
            word += character
        else:
            pirate_sentence += translate_pirate_word(word) + " "
            word = ""
    return pirate_sentence[0: -1]


# Main tests all the functions and reports on their results
def main():
    # testing the multiply function
    print("Testing the multiply function")
    print("""Testing multiply(2,3). Expecting a result of "6" and computed a result of""", str(multiply(2, 3)) + ".")
    print("""Testing multiply(5,6). Expecting a result of "30" and computed a result of""", str(multiply(5, 6)) + ".")
    print("""Testing multiply(0,4). Expecting a result of "0" and computed a result of""", str(multiply(0, 4)) + ".")
    print()

    # testing the choose_larger function
    print("Testing the choose_larger function")
    print("""Testing choose_larger(10, 20). Expecting a result of "20" and computed a result of""",
          str(choose_larger(10, 20)) + ".")
    print("""Testing choose_larger(-3,-3). Expecting a result of "-3" and computed a result of""",
          str(choose_larger(-3, -3)) + ".")
    print("""Testing choose_larger(7.5, 4/5). Expecting a result of "7.5" and computed a result of""",
          str(choose_larger(7.5, 4/5)) + ".")
    print()

    # testing the describe_number function
    print("Testing the describe_number function")
    print("""Testing describe_number(3). Expecting a result of "positive"
     and computed a result of""", describe_number(3) + ".")
    print("""Testing describe_number(0). Expecting a result of "zero" and computed a result of""",
          describe_number(0) + ".")
    print("""Testing describe_number(-5.3). Expecting a result of "negative" and computed a result of""",
          describe_number(-5.3) + ".")
    print()

    # testing the add_a_or_an_to_word function
    print("Testing the add_a_or_an_to_word function")
    print("""Testing add_a_or_an_to_word(octopus). Expecting a result of "an octopus" and computed a result of""",
          add_a_or_an_to_word("octopus") + ".")
    print("""Testing add_a_or_an_to_word(capybara). Expecting a result of "a capybara" and computed a result of""",
          add_a_or_an_to_word("capybara") + ".")
    print()

    # testing the add_a_or_an_or_any_to_word function
    print("Testing the add_a_or_an_or_any_to_word function")
    print("""Testing add_a_or_an_or_any_to_word(stairs). Expecting a result of "any stairs" and computed a result of""",
          add_a_or_an_or_any_to_word("stairs") + ".")
    print("""Testing add_a_or_an_or_any_to_word(chair). Expecting a result of "a chair" and computed a result of""",
          add_a_or_an_or_any_to_word("chair") + ".")
    print("""Testing add_a_or_an_or_any_to_word(orange). Expecting a result of "an orange" and computed a result of""",
          add_a_or_an_or_any_to_word("orange") + ".")
    print("""Testing add_a_or_an_or_any_to_word(apples). Expecting a result of "any apples" and computed a result of""",
          add_a_or_an_or_any_to_word("apples") + ".")
    print()

    # testing the collect_punctuation function
    print("Testing the collect_punctuation function")
    print("""Testing collect_punctuation("In the evening, I like to take my dog on a walk!! My dog's name is Fred.").
     Expecting a result of ",!!'." and computed a result of""",
          collect_punctuation("In the evening, I like to take my dog on a walk!! My dog's name is Fred.") + ".")
    print("""Testing collect_punctuation("Do you wanna build a snowman?").
     Expecting a result of "" and computed a result of""",
          collect_punctuation("Do you wanna build a snowman?") + ".")
    print()

    # testing the translate_pirate_word function.
    print("Testing the translate_pirate_word function")
    print("""Testing translate_pirate_word(hello).
     Expecting a result of "ahoy" and computed a result of""", translate_pirate_word("hello") + ".")
    print("""Testing translate_pirate_word(garbage).
     Expecting a result of "garbage" and computed a result of""", translate_pirate_word("garbage") + ".")
    print()

    # testing the translate_to_pirate function
    print("Testing the translate_to_pirate function")
    print("""Testing translate_to_pirate(yes you are a computer scientist).
     Expecting a result of "arr ye be a computer scientist" and computed a result of""",
          translate_to_pirate("yes you are a computer scientist") + ".")
    print("""Testing translate_to_pirate(hello he is my best friend).
     Expecting a result of "ahoy he be me best matey" and computed a result of""",
          translate_to_pirate("hello he is my best friend") + ".")
    print()


if __name__ == "__main__":
    main()
