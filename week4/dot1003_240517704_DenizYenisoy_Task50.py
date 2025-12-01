text = input("Please enter string:")
search_item = input("Please enter search item:")

index = text.find(search_item)

if index != -1:
    print(f"found it at {index}")
else:
    print("not found")