Hack = False
while not Hack:
    try:
        guess = int(input("enter a number: "))
        while guess%2 == 0:
            print("Get hacked or close program")
        Hack = True
    except ValueError:
        print("Guess")
