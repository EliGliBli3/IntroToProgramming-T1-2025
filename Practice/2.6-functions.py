MN_TAX_RATE = 0.06875

def calculate_tax(item, price, rate):
    print(f"Tax to be collected on {item}: {price*rate}\nTotal price: {price+(price*rate)}")

calculate_tax("Apple", 0.25, MN_TAX_RATE)

# Create a function called add five numbers that takes 5 parameters,
# one for each number. Print the sum of the 5 numbers.
# Run the function 3 times with different arguments.

def add_five_numbers(a, b, c, d, e):
    print(a+b+c+d+e)

add_five_numbers(1,2,3,4,5)
add_five_numbers(4,312,31,66,12)
add_five_numbers(100,99,98,97,96)

# Create a function called full_name that prints the concatenation of
# a person's first and last name.
# Take input using the input function, then run the function once.

def full_name(first, last):
    print(f"{first} {last}")

full_name(input("First name:\n>"), input("\nLast name:\n>"))

# Create a function called area_calculator that calculates the area
# of a rectangle. Take length and width as parameters.
# Run the function three times. No input.

def area_calculator(length, width):
    print(f"Area is " + str(length*width))

area_calculator(5, 1.23)
area_calculator(5, 1.23)
area_calculator(5, 1.23) # Did not specify different args.

# Create a function called word_smash that takes two parameters.
# The function should simply concatenate the two parameters.
# Convert the arguments to strings within the function to guard against
# non-string values.
# Run the function three times.

def word_smash(a, b):
    print(str(a)+str(b))

word_smash(1, " tafasdf")
word_smash(True, " that")
word_smash(0x0FF, " woaoaodfo")

# Create a function called echo that prints a string a number of times
# The function should take two parameters
#   - one for the string, one for the number of times.

def echo(message, num):
    print(str(message) * int(num))

echo("Echo, echo, echo\n", 5)

# Create a function called happy_birthday that takes one parameter: name
# When the function runs, it should print the happy birthday song for their name.
# Run it once

def happy_birthday(name):
    print(f"Happy birthday to you. Happy birthday to you. Happy birthday, dear {name}. Happy birthday to you.")

happy_birthday("Glorpus")

