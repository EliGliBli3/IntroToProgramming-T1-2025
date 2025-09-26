import os

def prompt_can_fly():
    os.system('cls')
    print("Please provide a 'y' for yes or an 'n' for no.")
    can_fly = input("\nCan your animal fly? (y/n)\n> ")
    if(can_fly.lower() == "y" or can_fly.lower() == "n"):
        return True if can_fly == 'y' else False
    return prompt_can_fly()

os.system('cls')
fav_animal = input("\nWhat is your favorite animal?\n> ")
os.system('cls')
reason = input("\nWhy is this your favorite animal?\n> ")
os.system('cls')
animal_sound = input("\nWhat sound does the animal make?\n> ")
os.system('cls')
animal_location = input("\nWhere does your animal come from?\n> ")
os.system('cls')
animal_size = input("\nIs your animal big or small?\n> ")
os.system('cls')
animal_fun_fact = input("\nWhat is one fun fact about your animal?\n> ")
os.system('cls')
animal_color = input("\nWhat color is your animal?\n> ")

animal_can_fly = prompt_can_fly()



os.system('cls')
summary = f"Your favorite animal is the {fav_animal.lower()} because {reason.lower()}." \
+f" It's {animal_size.lower()} sized, {animal_color.lower()}, and makes the {animal_sound.lower()} sound." \
+f" A fun fact about this animal is that {animal_fun_fact.lower()}." \
+f" This animal comes from {animal_location.lower()} and can {"" if animal_can_fly else "not "}fly."


print(summary)