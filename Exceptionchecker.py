try:
    num1, mun2 = eval(input("enter two numbers with a comma separating them \n"))
    answer = num1/mun2
    
except SyntaxError:
    print("Enter a comma between the numbers like 1, 2")
except ZeroDivisionError:
    print("Don't add a zero at the second number")
except: 
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print(answer)