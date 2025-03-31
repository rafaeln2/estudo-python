has_good_credit = True
has_high_income = False
has_criminal_record = True
house_price = 1000000

# if has_good_credit or has_high_income:
#     print("Eligible for loan")

# if has_good_credit and has_high_income:
#     print("Eligible for loan")

if has_good_credit or not has_criminal_record:
    print("Eligible for loan")
