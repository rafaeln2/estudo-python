import random
# import utils
from utils import highest_number
# from ..utils import highest_number
numbers = [random.randint(1, 100) for _ in range(10)]
print("Numbers: ", numbers)

# utils.highest_number(numbers)
highest_number(numbers)

# se for importar a classe, tem que chamar classe.metodo, ou importar direto o metodo utilizando from classe import metodo