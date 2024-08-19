def pass_class(course_percentage):
    return course_percentage >= 70


def main():
    print(pass_class(90))
    name = "Lucy Leary"
    print(len(name))
    for count in range(10):
        print(name[count])
    print(name[0:4])  # This is called a slice. It pulls out chunks of string.
    sum_total = 0
    n = 5
    for number in range(1, n + 1):
        sum_total = sum_total + number
    print(sum_total)
    text = ("I like to go running on the weekends. But I hate going running during the week. It takes up too much "
            "time, and I'm just way too busy for that. But good for you though. I'm glad you still find time to run"
            "as often as you seem to. But I am a little jealous, even though I don't like to admit that.")
    number_of_e = 0
    for count in range(0, len(text) - 1):
        if text[count] == "e":
            number_of_e = number_of_e + 1
    print(number_of_e)


if __name__ == "__main__":
    main()

# We can't change a single index of a string. We can only reassign the whole string.
# elif means else if

# IN CLASS PRACTICE ASSIGNMENT:

def status_from_age(age):
    if age < 1:
        return "baby"
    elif age < 18:
        return "minor"
    else:
        return "adult"


print(status_from_age(18))
