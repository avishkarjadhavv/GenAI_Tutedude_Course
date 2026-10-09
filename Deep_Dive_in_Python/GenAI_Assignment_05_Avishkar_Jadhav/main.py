
# Task 1 - Import math_utils
import math_utils

print("Task 1 - Math Utilities")
print("Addition:", math_utils.add(10, 5))
print("Subtraction:", math_utils.subtract(10, 5))
print("Square:", math_utils.square(4))

# Second import method
from math_utils import square

print("Square using direct import:", square(6))


# Task 2 - Import string_utils
import string_utils

print("\nTask 2 - String Utilities")
text = "python modules and packages"

print("Capitalized:", string_utils.capitalize_words(text))
print("Reversed:", string_utils.reverse_string(text))
print("Word count:", string_utils.word_count(text))


# Task 4 - Import shop_package
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax

print("\nTask 4 - Shop Package")
print("Discounted price:", disc.apply_discount(1000, 10))
print("Price after flat discount:", disc.flat_discount(1000))
print("Total bill:", calculate_total([100, 200, 300]))
print("Bill after 5% tax:", apply_tax(1000))
