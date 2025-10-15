try:
    x = int(input("First Number: "))
    y = int(input("Second Number: "))
    print(x/y)
except ValueError:
    print("Please enter a Valid number next time!")
except ZeroDivisionError:
    print("Cannot Divide by Zero!")