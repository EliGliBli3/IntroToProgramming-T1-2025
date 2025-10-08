score = 0

answer_1 = input("What is 2 + 2?\n>")
answer_2 = input("\nHow many fingers are on one hand?\n>")
answer_3 = input("\nWhat is the diameter of the sun kilometers? (numbers, no commas)\n>")
answer_4 = input("\nWhen is noon?\n>")
answer_5 = input("\nHow many questions have you answered?\n>")
answer_6 = input("\nHow many minutes are in one hour?\n>")
answer_7 = input("\nWhat is the 7th month on the gregorian calendar?\n>")
answer_8 = input("\nHow many hands are on a clock?\n>")
answer_9 = input("\nWhich number question are you on NOW?\n>")
answer_10 = input("\nDid you enjoy this quiz?\n>")

def tally_score():
    global score
    if answer_1 == "4" or answer_1.lower() == "four": score+=1
    if answer_2 == "5" or answer_2.lower() == "five": score+=1
    if 13927000 - int(answer_3) < 100000: score+=1
    if answer_4 == "12:00" or answer_4.lower() == "12 pm": score+=1
    if answer_5 == "4" or answer_5.lower() == "four": score+=1
    if answer_6 == "60" or answer_6.lower() == "sixty": score+=1
    if answer_7.lower() == "july": score+=1
    if answer_8 == "3" or answer_8.lower() == "three": score+=1
    if answer_9 == "9" or answer_9.lower() == "nine": score+=1
    if answer_10.lower() == "yes": score+=1

tally_score()
print(f"Finished quiz. Scored {score}/10")