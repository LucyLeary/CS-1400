first_name = input("Tell me your first name. ")
last_name = input("Tell my your last name, " + first_name + ". ")
print("Your name is " + first_name + " " + last_name + ".")
print(first_name + ", I am your father, Mr. " + last_name + ".")
number_of_fathers = 5
while number_of_fathers in range(10):
    number_of_fathers = number_of_fathers + int(number_of_fathers/2)
    print(number_of_fathers)