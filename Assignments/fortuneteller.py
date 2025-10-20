import random

def lucky_num():
    msg = input("Enter your lucky number:\n>")
    try:
        result = int(msg)
        return result
    except:
        print("Please enter a whole number")
        return lucky_num()
def years():
    msg = input("How many years into the future would you like to see?\n>")
    try:
        result = float(msg)
        return result
    except:
        print("Please enter a number")
        return years()
def magic_mult():
    msg = input("Enter a magic multiplier:\n>")
    try:
        result = float(msg)
        return result
    except:
        print("Please enter a number")
        return magic_mult()

fortune_value = abs(years()/lucky_num()) * magic_mult() / random.randrange(1, 3)

if fortune_value < 1:
    print("You will live in the place of your dreams.")
if 1 <= fortune_value < 2:
    print("Nothing will change, and you will continue on your journey.")
if 2 <= fortune_value < 4:
    print("You will experience hardships, but perservere")
if 4 <= fortune_value < 16:
    print("You will find yourself in a great struggle.")
if fortune_value >= 16:
    print("You will lose someone very close to you.")   # maybe a bit dark, but hey.