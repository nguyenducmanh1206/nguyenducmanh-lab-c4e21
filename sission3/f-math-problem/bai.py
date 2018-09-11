while True :
    from random import randint, choice 
    from calc2  import calculate
    x=randint(0, 9)
    y=randint(0, 9)
    op = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)
    # d=(x + y) +  error 
    # c=x + y
    r = calculate(x, y, op) + error
    print(x, op, y, "=", r)
    x=input("T/F ").upper()
    if calculate(x, y, op) == r:
        # if d != c:
    #  x=input("T/F ").upper()
        
        if x == "T":
            print("F")
        elif x == "F":
                print("F")
    else:
        if x == "T":
            print("F")
        elif x =="F" :
            print("F")
    
    # elif d == c:
    #     m=input("T/F").upper()  
    #     if m == "T":
    #         print("T")
    #     elif x =="F":
    #         print("F")
















