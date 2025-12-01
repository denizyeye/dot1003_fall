sentence = "The quick brown fox jumps over the lazy dog"
search_item = input("Which item do you want to search? ")

count = sentence.count(search_item)
print(f"item {search_item} appeared {count} times")