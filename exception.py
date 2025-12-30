#program to handle a ZeroDivisionError
n = int(input("enter num1 "))
m=int(input("enter num2 "))
try:
    val=n/m
    print(val)
except ZeroDivisionError:
    print("any value cannot be divided by zero")

#program that accepts user input and handles a ValueError
try:
    i=int("apple")
    print(i)
except ValueError:
    print("Not an integer - Error!!")

#program to open a file and handle a FileNotFoundError
try:
    f = open("file.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not found!!")

#program that uses try, except, else, and finally block
n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
try:
    result = n1 / n2
except ZeroDivisionError:
    print("Error!! Cannot divide by zero")
except ValueError:
    print("Error!! not an integer")
else:
    print(result)
finally:
    print("Execution completed.")

#handle multiple exceptions in a single try block
n= int(input("Enter n: "))
m = int(input("Enter m: "))
r=n/m
try:
    print(r)
except ZeroDivisionError:
    print("Error!! Cannot divide by zero")
except ValueError:
    print("Error!! not an integer")
except Exception:
    print("error!!!")


