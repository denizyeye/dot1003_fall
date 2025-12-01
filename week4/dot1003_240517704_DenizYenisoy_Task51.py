sentence = "The quick brown fox jumps over the lazy dog"
my_flag = True

while my_flag:
    search_item = input("What are you looking for? ")
    
    if search_item == "-1":
        print("Bye.")
        my_flag = False
    else:
        index = sentence.find(search_item)
        if index != -1:
            print(f"found it at {index}")
        else:
            print("not found")