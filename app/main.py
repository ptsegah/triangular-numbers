from fastapi import FastAPI
import math

app = FastAPI()

# an example for triangular numbers

@app.get("/")
def index():
    return "Hey!, I determine triangular numbers."


# determining triangular numbers
# a number is said to be triangular if 8x + 1 is equal to a perfect square

@app.get("/triangular-numbers")
def triangular_number(num: int):
    if num < 0:
        return False
    
    is_triangular = True

    test = 8*num + 1
    root = int(math.sqrt(test))
    # ~ ignore this rule: the condition requires the square root of (8x + 1) must be an odd integer to qualify as a triangular number.

    return root * root == test
       
# testing the code

# print(triangular_number(55))
# print(triangular_number(7))