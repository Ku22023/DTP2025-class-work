from random import sample

list = ["r", "p", "s"]

def get_user_input():
    user_input = str(input("Type:\nP for Paper \nS for Scissor \nR for Rock\n"))
    if user_input == "p" or user_input == "s" or user_input == "r":
        return user_input
    else:
        print("Please enter a valid argument.")


def generate_item():
    gen_option = sample(list, 1)
    return gen_option

def whowins(user_input, gen_option):
    if user_input == gen_option:
        print("you tied!")
    elif user_input == "r" and gen_option == "s":
        print("You won!")
    elif user_input == "s" and gen_option == "p":
        print("You won!")
    elif user_input == "p" and gen_option == "r":
        print("You won!")
    else:
        print("you lost!")
    print(f"Computer chose: {gen_option}")
    print(f"You chose: {user_input}")


games = 0
wins = 0
lost = 0
print(f"Welcome to paper scisscors rock! \n You've won: {wins} \n You've played: {games} \n You've lost: {lost}")
user_input = get_user_input()
gen_option = generate_item()
whowins(user_input,gen_option)