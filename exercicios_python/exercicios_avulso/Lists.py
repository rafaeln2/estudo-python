# names= ["rafa", "luan", "andre", "joao", "mario"]
# print(names[2:4])
# names.remove(0)
# print(names)

import random
numbers = [random.randint(1, 100) for _ in range(10)]
print("Numbers: ", numbers)

# highest_number = numbers[0]
# for numberX in numbers:
#     for numberY in numbers:
#         if numberY > highest_number:
#             highest_number = numberY
#     if highest_number == numberX:
#         print("The highest number is: ", highest_number)
#         break
    
highest_number = numbers[0]
for numberX in numbers:
    
    if numberX > highest_number:
        highest_number = numberX
print("The highest number is: ", highest_number)
    