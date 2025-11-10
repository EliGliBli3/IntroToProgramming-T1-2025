import time, os, math, random

def prompt_assignment():
    os.system('cls')
    msg = input("Assignment view? (y/n)")
    result = False
    match msg.lower():
        case 'y': result = True
        case 'n': result = False
        case _: result = None
    return result if result != None else prompt_assignment()
assignment = prompt_assignment()


if not assignment:
    games = ["Elden Ring", "Shadow of the Colossus", "Diablo III", "Minecraft", "Super Mario World"]

    for game in games:
        print(game)
        
    for i in range(0,101,10):
        print(i)

    for i in [random.randint(-100, 100) for j in range(100)]:
        if i>0: print(i)
else:
# PRACTICE ASSIGNMENT

    for i in range(1, 11)[::-1]:
        print(i)
    
    l1 = range(10)
    print(sum(l1))
    
    l2 = range(1,6)
    l2_squared = [i**2 for i in l2]
    print(l2_squared)
    
    msg = input("Enter a string\n>")
    vowel_count = 0
    for c in msg:
        if c in "aeiou": vowel_count+=1
    print(vowel_count)
    
    mult_table = input("Enter a number\n>")
    try:
        for i in range(10):
            print(f"{mult_table} x {i+1} = {float(mult_table)*(i+1)}")
    except:
        print("That's not a number. No second chances.")
    
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        print(f"{"Goodbye" if name == "Charlie" else "Hello"}, {name}!")