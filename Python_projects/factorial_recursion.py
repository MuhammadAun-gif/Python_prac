def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
x = input("Enter a number for Factorial calculation: ")
x = int(x)

result = factorial(x)
print("The factorial is: {}".format(result))