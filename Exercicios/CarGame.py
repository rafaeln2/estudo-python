
current_input: str = ""
is_started = False
while True:
    current_input = input(">").lower()
    if current_input == "start":
        if is_started:
            print("Car already turned on.")
            continue
        print("Car turned on.")
        is_started = True
    elif current_input == "stop":
        if not is_started:
            print("Car already turned off.")
            continue
        print("Engine turned off.")
        is_started = False
    elif current_input == "quit":
        print("Quitting the app.")
        break;
    elif current_input == "help":
        print("""All commands:
Start: turns on engine
Stop: turns on engine
Quit: shutdowns application""")
    else:
        print("Invalid command.")

print("Thank you for playing")
