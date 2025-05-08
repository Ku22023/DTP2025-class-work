answer = input(int("What is the sum of 5 and 10?"))
try:
    answer + 1
except NameError:
    
    if answer == 15:
        print("Hooray!")
    else:
        print(f"sorry! {answer} is wrong wrong wrong")