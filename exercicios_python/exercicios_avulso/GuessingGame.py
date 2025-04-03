# secret_number = 9
# number_guessed = 0
# while number_guessed != secret_number:
#     number_guessed = int(input("Guess: "))
# print("You win!")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    number_guessed = int(input("Guess: "))
    if number_guessed == secret_number:
        print("you win!")
        break
    guess_count += 1
else:
    print("you lost!")
