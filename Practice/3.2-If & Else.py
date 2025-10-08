real_password = "Knights25"

def prompt_password():
    submitted_password = input("What is the password?\n>")

    if submitted_password == real_password:
        print("Access granted.")
    else:
        print("Access denied.")
        prompt_password()

prompt_password()