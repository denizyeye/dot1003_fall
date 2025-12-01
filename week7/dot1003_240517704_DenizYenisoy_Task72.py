my_set = set()
my_flag = True

while my_flag:
    element = input("Enter an element for set:")
    
    if element == "exit":
        my_flag = False
    else:
        if element in my_set:
            print(f"{element} is already in our set.")
        else:
            my_set.add(element)

for item in my_set:
    print(item)