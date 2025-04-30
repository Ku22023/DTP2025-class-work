word = "kyle"
guesses = 10
letter1 = "_"
letter2 = "_"
letter3 = "_"
letter4 = "_"
alreadyguessed = []

while guesses >= 0:
    if letter1 == "k" and letter2 == "y" and letter3 == "l" and letter4 == "e":
        print("you win! the word was: k y l e")
        guesses = -10
    else:
        answer = str(input("Guess a letter \n" 
        f"Current guesses: {letter1} {letter2} {letter3} {letter4} \n" ))
#        alreadyguessed.append(answer)
#        if alreadyguessed not in 
        if answer != "k":
            if answer != "y":
                if answer != "l":
                    if answer != "e":
                        print(f"wrong! Tries left: {guesses} \n")
                        guesses -= 1
                    else:
                        letter4 = "e"
                        print("You got it right!")
                else:
                    letter3 = "l"
                    print("You got it right!")
            else:
                letter2 = "y"
                print("You got it right!")
        else:
            letter1 = "k"
            print("You got it right!")
else:
    if guesses != -10:
        print("you lose!!!")