try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError as e:
    print("Invalid input, please enter a number.")
except TypeError as e:
    print(e)


