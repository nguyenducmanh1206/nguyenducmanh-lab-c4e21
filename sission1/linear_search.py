items=[8, 9, 10, -1, 23, 45, 99, -76]

x=int(input("nhap so :"))
# found = False
for index, item in enumerate(items):
    if x == item:
        # found = True
        print("tim thay")
        print("thuoc vi tri", index)
        break # find one
else :       
# if found == False:
    print("khong tim thay")
