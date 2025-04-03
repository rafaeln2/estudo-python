def highest_number(numbers):
    highest_number = numbers[0]
    for numberX in numbers:
        if numberX > highest_number:
            highest_number = numberX
    print("The highest number is: ", highest_number)
    