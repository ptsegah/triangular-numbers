# determining triangular numbers
# a number is said to be triangular if 8x + 1 is equal to a perfect square
import math

def triangular_number(num: int):
    if num < 0:
        return False
    
    is_triangular = True

    test = 8*num + 1
    root = int(math.sqrt(test))
    # ~ ignore this rule: the condition requires the square root of (8x + 1) must be an odd integer to qualify as a triangular number.

    return root * root == test
       
# testing the code

print(triangular_number(55))
print(triangular_number(7))