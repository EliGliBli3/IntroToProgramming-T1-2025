#   Problem 1:

first_word = input("Enter first word : ")
second_word = input("Enter second word : ")
third_word = input("Enter third word : ")

print(first_word + second_word + third_word)    # Concat with no delimiters

#   Problem 2:

def add_three(a, b, c):
    print(a + b + c)    # Print the sum of integers a, b, and c.

first_number = int(input("Enter first whole number : "))
second_number = int(input("Enter second whole number : "))
third_number = int(input("Enter third whole number : "))

add_three(first_number, second_number, third_number)

#   Problem 3:

def data_three():
    word = input("Enter a word : ")
    _int = int(input("Enter a whole number : "))
    _float = float(input("Enter any number : "))

    print(str(_int + _float) + word)
