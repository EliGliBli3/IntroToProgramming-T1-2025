import math

answer = float(input("\nEnter a whole number\n>"))
print(math.trunc(answer) == answer)

answer = float(input("\nEnter a number less than 10\n>"))
print(answer < 10)

answer = input("\nEnter \"green\" (case sensitive)\n>")
print(answer == "green")

answer = float(input("\nEnter 5 or a number greater than 47\n>"))
print(answer == 5 or float(answer) > 47)

answer = float(input("\nEnter a number that is divisible by 4\n>"))
print(answer % 4 == 0)

answer = float(input("\nEnter a number between 4 and 6 (exclusive)\n>"))
print(answer > 4 and answer < 6)

answer = float(input("\nEnter a number between -4 and 18 (inclusive)\n>"))
print(answer >= -4 and answer <= 18)
