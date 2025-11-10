import random, os

num = random.randint(1, 100)
guess = 0

while guess != num:
    def prompt_guess():
        msg = input("Guess a whole number\n>")
        try:
            i_msg = int(msg)
            return i_msg
        except:
            os.system('cls')
            print("Please enter a whole number.")
            return prompt_guess()
    guess = prompt_guess()
    
    os.system('cls')
    
    print(
        f"{guess} is too low" 
        if guess < num else 
            (f"{guess} is too high" 
             if guess > num 
             else f"Congratulations! You correctly guessed {num}")
    )