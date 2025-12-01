def search_in_data():
    data_input = input("Enter the input to search:")
    search_item = input("Which item do you want to search?:")
    
    count = data_input.count(search_item) 
    print(f"item {search_item} appeared {count} times")

search_in_data()