try:
    Age = int(input("Input your age: "))
    print("Your age,",Age, "was successfully stored in our datastores")

except ValueError:
    print("Enter a valid number(s)")