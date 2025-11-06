import os

fav_fruits = ["apple", "Apple", "banana", "orange", "Banana"]
print(fav_fruits[0])
print(fav_fruits[-1])

fav_fruits.append(input("Add a fruit to the list\n>"))
def prompt_remove():
    try:
        remove = input(f"Select item to remove:\n{"\n".join(fav_fruits)}\n\n>")
        fav_fruits.remove(remove)
    except:
        os.system('cls')
        prompt_remove()
prompt_remove()

fav_fruits.sort()
print(f"\nApple appears {[f.lower() for f in fav_fruits].count("apple")} times.\n")

for f in fav_fruits:
    print(f)