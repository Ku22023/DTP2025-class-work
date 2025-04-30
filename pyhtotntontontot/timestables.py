try:
    inpnum = int(input("Enter a number: "))
    multiplier = int(input("What would you like to multiply up to? "))
    for i in range(1,multiplier + 1):
        print(f"{inpnum} * {i} = {inpnum * i}")


except ValueError:
    print("oooops")
    print("Please restart")