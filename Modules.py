import converters
print(converters.kg_to_lbs(70))


# other approach for calling modules

from converters import kg_to_lbs
kg_to_lbs(100)


from converters import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum)

from ecommerce.shipping import calc_shipping

# every module from the shipping file

from ecommerce import shipping