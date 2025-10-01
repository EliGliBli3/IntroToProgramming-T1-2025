import os

'''
Today I went to my favorite Taco Stand called the {adj} {animal}. 
Unlike most food stands, they cook and prepare the food in a {thing you ride in} while you {verb}. 
The best thing on the menu is the {color} {noun}. 
Instead of ground beef they fill the taco with {food plural}, cheese, and top it off with a salsa made from {food plural}.
If that doesn't make your mouth water, then it's just like {person} always says: {saying}!

Credit: Price Stern Sloan, "Mad Libs"

----
Steps to creation
----

- Ask user for 10 questions, looping and switching the question
- Store each answer in a list
- Concat each word in the list in order into the MadLib.


'''
input_list = []
def print_mad_lib():
    global input_list

    print(f"Today I went to my favorite Taco Stand called the {input_list[0]} {input_list[1]}. " \
    + f"Unlike most food stands, they cook and prepare the food in a {input_list[2]} while you {input_list[3]}. " \
    + f"The best thing on the menu is the {input_list[4]} {input_list[5]}. " \
    + f"Instead of ground beef they fill the taco with {input_list[6]}, cheese, and top it off with a salsa made from {input_list[7]}. " \
    + f"If that doesn't make your mouth water, then it's just like {input_list[8]} always says: {input_list[9]}!\n\n")
for i in range(10):
    os.system('cls')    # clear the console
    
    input_type = ""
    match i:    # set each input type in order
        case 0: input_type = "n adjective"
        case 1: input_type = "n animal"
        case 2: input_type = " thing you ride in"
        case 3: input_type = " verb"
        case 4: input_type = " color"
        case 5: input_type = " noun"
        case 6: input_type = " food, plural"
        case 7: input_type = " food, plural"
        case 8: input_type = " person"
        case 9: input_type = " saying"
    input_list.append(input(f"Enter a{input_type}:\n> "))
os.system('cls')    # clear the console
print_mad_lib()
