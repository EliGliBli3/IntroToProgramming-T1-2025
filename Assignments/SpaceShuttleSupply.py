import os

os.system('cls')
print("Preparing for takeoff. Please confirm the following:\n")
countdown = input("Seconds until launch > ")
os.system('cls')

print("Please provide the quantities aboard for the following:")
oxygen_tanks = input("\nOxygen tanks > ")
food_packs = input("Food Packs > ")
water_packs = input("Water Packs > ")

os.system('cls')
print(f"Entered supplies:\nOxygen Tanks: {oxygen_tanks}\nFood Packs: {food_packs}\nWater Packs: {water_packs}")
oxygen_tanks = input("\nPlease reconfirm oxygen tank supply.\n> ")

os.system('cls')
print(f"All supplies confirmed:\nOxygen Tanks: {oxygen_tanks}\nFood Packs: {food_packs}\nWater Packs: {water_packs}\n\nTime until takeoff: {countdown} seconds")