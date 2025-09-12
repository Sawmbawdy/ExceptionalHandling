try:
    Age = int(input("Input your age: "))
    print("Your age,",Age, "was successfully stored in our datastores")
    if Age%2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

except ValueError:
    print("Enter a valid number(s)")
