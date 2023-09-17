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

test()
