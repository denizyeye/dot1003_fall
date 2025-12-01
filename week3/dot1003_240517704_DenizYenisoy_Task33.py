myflag=True
mylist=[]
while myflag:
    userinp=input("please enter an input:")
    if userinp=="exit":
        myflag = False
    else:
        mylist.append(userinp)
print(mylist)