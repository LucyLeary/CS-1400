fruit = {'apples': 10, 'grapes': 20}
print(fruit)
fruit['apples'] = 15
print(fruit)
fruit['pears'] = 5
print(fruit)
print(fruit['apples'])  # if you call a key that doesn't exist, will get an error
print(fruit.get('lemons'))  # use this method if you're not sure if key exists
print(fruit.get('lemons', 0))  # second parameter changes what's returned from None to something else
print(fruit.get('apples', 0))
print('apples' in fruit)  # checks if in dictionary, returns true or false


for key in fruit:
    print("key:", key + ":", fruit[key])

# MY VERSION create inventory management system

fruit = {}
while True:
    print("commands are:")
    print("  - set kind_of_fruit number")
    print("  - print kind_of_fruit")
    print("  - print")
    print("  - stop")

    text = input('What do you want to do? ')
    commands = text.split()  # takes input from user and turns words into list of strings
    print(commands)
    if commands[0] == 'stop':
        break
    elif commands[0] == 'set':
        fruit[commands[1]] = commands[2]
    elif commands[0] == 'print':
        if len(commands) == 1:
            for key in fruit:
                print("There are", fruit[key], key)
        else:
            print(fruit.get(commands[1], 0))


# Here is the CLASS EXAMPLE script for this lab
"""
A sample script to manage fruit types and the number of them.
"""
# The fruit dict holds key string with the fruit name and a number value.
fruit = {}
while True:
    # Display command options to the user
    print("commands are:")
    print("  - set kind_of_fruit number")
    print("  - print kind_of_fruit")
    print("  - print")
    print("  - stop")

    # Ask for the command and break it into words
    text = input('What do you want to do? ')
    commands = text.split()
    print(commands)

    # Check the first word for the command type
    if commands[0] == 'stop':
        break
    elif commands[0] == 'set':
        fruit[commands[1]] = int(commands[2])
    # The print command has two options
    elif commands[0] == 'print':
        if len(commands) == 1:
            for key in fruit:
                print("There are " + str(fruit[key]) + " " + key)
        else:
            # If the fruit is not there, use 0.
            print(fruit.get(commands[1], 0))
