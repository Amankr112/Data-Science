# Exception handling in python :
'''
try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    res = num1/num2
    print('Resultant is:', res)
    
except:
    print("Enter the valid number and second number should not be zero")

'''


# except Exception as variable name in python :
'''
try :
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    res = num1/num2
    print('Resultant is:', res)
    
except Exception as e:
    print(e)
'''


# We can handle exception with the help of exception name in python and have multiple except blocks in python :
'''
try: 
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    res = num1/num2
    print('Resultant is:', res)
    
except ZeroDivisionError:
    print("You cannot divide a number by zero")
    
except ValueError:
    print("Please enter a valid number")
'''


# How to raise custom exception in python :
'''
name = input("Enter your name:")
if name == 'Mudit':
    raise ValueError("Mudit is not allowed")
else:
    print("Hello", name)

'''


# try - except - else block in python :
try :
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    res = num1/num2
    
except Exception as e:
    print(e)
    
else:
    print('Resultant is:', res)



# try and except block with finally block in python :
'''
try:
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    res = x/y
    print(res)

except Exception as e:
    print(e)

finally:
    print("Finally block will run at any cost")
    
'''
    