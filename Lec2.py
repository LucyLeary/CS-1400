# HOW TO REPEAT CODE #
for count in range(3):
    age = input('How old are you? ')
    next_age = int(age) + 1
    print("Next year you will be", next_age)
    print(count+int(age)//3)
# input() always produces a string #

# PRACTICE GRADESCOPE PROBLEM (SOLVED 2 WAYS): #
countdown = 11
for count in range(10):
    countdown = countdown - 1
    print(countdown)
print("Launch")

for count in range(10):
    print(10 - count)
print("Launch")
