def get_even_list(s):
    new=[]  
    for i in s :
        if i % 2 ==0:
            new.append(i)
    return new

even_list = get_even_list([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
   print("Your function is correct")
else:
   print("Ooops, bugs detected")
