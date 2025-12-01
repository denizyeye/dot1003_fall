my_set = set()
my_flag = True

while my_flag:
    element = input("Enter an element for set: ")
    
    if element == "exit":
        my_flag = False
    else:
        my_set.add(element)

for item in my_set:
    print(item)