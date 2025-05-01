from random import sample

list = ["r", "p", "s"]

def get_user_input():
    user_input = str(input("Type P for Paper \n S for Scissor \n R for Rock"))
    return user_input

def generate_item():
    option = sample(list, 1)
    return option

def whowins(user_input, option, wins, games, lost):
    if user_input == option:
        print(f"You chose {user_input}")
    else:
        if user_input == "r":
            if option == "s":
                print("You chose Rock and the Robot chose Scissors! \n You win!")
                wins += 1
                return wins
            elif option == "s"
    games += 1
    return games

games = 0
wins = 0
lost = 0
print(f"Welcome to paper scisscors rock! \n You've won: {wins} \n You've played: {games} \n You've lost: {lost}")
