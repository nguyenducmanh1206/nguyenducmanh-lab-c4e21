def get_even_list(s):
    new=[]  
    for i in s :
        if i % 2 ==0:
            new.append(i)
    print(new)        
s=[2, 3, 4, 9, 5, 10, -2, -3]
get_even_list(s)




