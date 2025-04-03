# customer = {
#     "name": "Lucas",
#     "age": 25,
#     "is_verified": True
# }

# print(customer["name"])
# print(customer.get("teste","Nome padrão"))

phone = input("Phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
for number in phone:
    print(digits_mapping.get(number, "!"))