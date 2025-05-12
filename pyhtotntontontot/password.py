password = "kylekyle"
attempts = 5

while attempts > 0:
    answer = str(input("Enter the password! "))
    if answer != password:
        attempts -= 1
        print(f"Sorry! '{answer}' is wrong! You have {attempts} attempts remaining.")
    else:
        print("Welcome! password is correct")
        print(f"you took {5 - attempts} tries")
        attempts = 0