items=[4, 6, 78, -90, 78, 67, 100]
x= int(input("nhap so : "))
if x in items :
    print("found")
    found_index=items.index(x)
    print("vi tri", found_index)
else:
    print("not found")




