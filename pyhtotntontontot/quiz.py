score = 0
try:
    answer = int(input("what is the sum of 10 and 5? "))
except ValueError:
    print("sorry thats wrong!")
    answer = str(input("What city has the eiffel tower? "))
    answer = answer.lower()
    if answer == "paris":
        print("yabbadabbadoo!")
        score += 1
    else:
        print("wrong agagin!!!!!")
    answer = str(input("What country is the eiffel tower in? "))
    answer = answer.lower()
    if answer == "france":
        print("Yahoooo!")
        score += 1
    print(f"your score was {score}")
else:
    if answer == 15:
        print("yipee dipee doo!")
        score += 1
    else:
        print("sorry u got it wrong")
    answer = str(input("What city has the eiffel tower? "))
    answer = answer.lower()
    if answer == "paris":
        print("yabbadabbadoo!")
        score += 1
    else:
        print("wrong agagin!!!!!")
    answer = str(input("What country is the eiffel tower in? "))
    answer = answer.lower()
    if answer == "france":
        print("Yahoooo!")
        score += 1
    print(f"your score was {score}")