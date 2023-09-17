# print("Hello World")

# Declaring Variables
# checklist = list()

# Can also be written like this:
# checklist = []

# Making Code Reusable with Functions
# def my_fun_function(say_this):
#     print(say_this)

# my_fun_function('Hello World')

# Library to be able to clear terminal
import os

# Library to be able to color text in terminal
from termcolor import colored

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
        string = checklist[index]
        if string[0] == "√":
            string = string[2:]
        else:
            string = string
        split_string = string.split()
        color = split_string[0]
        print(colored("{} {}".format(index, list_item), color))
        index += 1

## Mark items as completed
def mark_completed(index):
    checked_item = "√ " + checklist[index]
    update(index, checked_item)
    return checklist[index]

## Unmark items
def unmark(index):
    checked_item = checklist[index]
    is_not_marked = True
    while is_not_marked:
        if checked_item[0] == "√":
            is_not_marked = False
            unchecked_item = checked_item[2:]
            update(index, unchecked_item)
            return checklist[index]
        elif index == 'Q' or index == 'q':
                exit()
        else:
            print("Please pick a checked item. Press Q to quit\n")
            index = (user_input("Index number? "))

## Get input from the user
def user_input(prompt):
    user_input = input(prompt)
    return user_input

## Check if index input by the user is valid
def is_input_valid(input_index):
    is_not_valid = True
    while is_not_valid:
        if input_index.isdigit() and int(input_index) in range(0, len(checklist)):
            is_not_valid = False
            return int(input_index)
        elif input_index == 'Q' or input_index == 'q':
            exit()
        else:
            print("Please input a valid index number. Press Q to quit\n")
            input_index = (user_input("Index number? "))
            

## Select which functions to run
def select(function_code):
    # Create item
    if function_code == "A":
        input_item = user_input("Input item: ")
        create(input_item)
        os.system('clear')

    # Read item
    elif function_code == "R":
        item_index = (user_input("Index number? "))
        item_index = is_input_valid(item_index)
        read(item_index)

    # Update item
    elif function_code == "C":
        item_index = (user_input("Which index number would you like to change? "))
        item_index = is_input_valid(item_index)
        input_item = user_input("What item would you like to change it with? ")
        update(item_index, input_item)
        os.system('clear')

    # Destroy item
    elif function_code == "D":
        item_index = (user_input("Which index number would you like to delete? "))
        item_index = is_input_valid(item_index)
        destroy(item_index)
        os.system('clear')

    # Mark item
    elif function_code == "M":
        item_index = (user_input("Which index number would you like to mark? "))
        item_index = is_input_valid(item_index)
        mark_completed(item_index)
        os.system('clear')

    # Unmark item
    elif function_code == "U":
        item_index = (user_input("Which index number would you like to unmark? "))
        item_index = is_input_valid(item_index)
        unmark(item_index)
        os.system('clear')        

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Stop the loop
    elif function_code == "Q":
        os.system('clear')
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

# test()

running = True
while running:
    print("Your color options are grey, red, green, yellow, blue, magenta, cyan, and white.")
    selection = user_input("Press:\nA to add to list,\nC to update an item on the list,\nD to delete an item from the list,\nR to read from list,\nM to mark item as completed,\nU to unmark item,\nP to display list,\nand Q to quit:\n").upper()
    running = select(selection)