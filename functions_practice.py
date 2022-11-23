# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
def hello():
    print("Hello, Instructor!!")

# added this just so when i did the python in terminal I would be able to see the functions seperated
def new_line():
    print("---------------------")

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(yesterday, today, tomorrow):
    return [yesterday, today, tomorrow]

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say 
# "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). 
# If the list is empty, print "My lunchbox is empty!". The function should not return anything.
def eat_lunch(sandwich):
    if len(sandwich) == 0:
        print("My lunch is empty!")
    else:
        for s in range(len(sandwich)):
            if s == 0:
                print(f"First I eat {sandwich[0]}")
            else:
                print(f"Next I eat {sandwich[s]}")



hello()
new_line()
print(pack("yesterday","today","tomorrow"))
new_line()
print(pack(1,2,3))
new_line()
eat_lunch([])
new_line()
eat_lunch(["sandwich"])
new_line()
eat_lunch(["Strawberries","Watermelon","Ice Cream","Chips Ahoy"])