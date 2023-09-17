# print("Hello World")

# Declaring Variables
# checklist = list()

# Can also be written like this:
# checklist = []

# Making Code Reusable with Functions
# def my_fun_function(say_this):
#     print(say_this)

# my_fun_function('Hello World')

# Create, Read, Update, and Destroy (CRUD)
## Create 
checklist = list()
# checklist.append('Blue')
# print(checklist)
# checklist.append('Orange')
# print(checklist)

### Add item to list
def create(item):
    checklist.append(item)

## Read - Access item on the list
def read(index):
    return checklist[index]

## Update - Overwrite data located at a specified index
def update(index, item):
    checklist[index] = item

## Destroy - Remove items from the list
def destroy(index):
    checklist.pop(index)

# Helper Functions
## View the entire list at once
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

## Mark items as completed
def mark_completed(index):
    checked_item = "√ " + checklist[index]
    update(index, checked_item)
    return checklist[index]


def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

## Select which functions to run
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index Number? "))

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Stop the loop
    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")

    return True

# Testing
def test():
    create('purple sox')
    create('red cloak')

    print(read(0))
    print(read(1))

    update(0, 'purple socks')
    destroy(1)

    print(read(0))
    # print(read(1))

    list_all_items()

    # Call your new function with the appropriate value
    select("C")

    # View the results
    list_all_items()

    # Call function with new value
    select("R")

    # View results
    list_all_items()

test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit:\n")
    running = select(selection)