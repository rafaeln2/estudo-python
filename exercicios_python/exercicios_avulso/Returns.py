def square(number):
    return number * number

square_func = square(3)

print(square_func)

print(square(3))

print((lambda x: x * x)(3))
print(lambda x: 3*3)