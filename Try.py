try: 
    inp = int(input("age is: "))
    print(inp)
except ValueError as ex:
    print("Exception:", ex)