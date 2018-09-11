from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x=randint(0, 9)
    y=randint(0, 9)
    op = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)
    r = (x + y) + error
    

    
    return [x, y, "+", r]

def check_answer(x, y, op, result, user_choice):
    print("check answer:", user_choice)
   
    return False
   
    pass
