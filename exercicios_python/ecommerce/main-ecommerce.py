# import ecommerce.shipping # 1
# from ecommerce.shipping import calc_shipping # 2
from ecommerce import shipping # 3

# ecommerce.shipping.calc_shipping() # 1
# calc_shipping # 2

shipping.calc_shipping() # 3