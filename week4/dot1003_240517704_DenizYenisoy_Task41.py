def check_length(word1, word2):
    if len(word1) > len(word2):
        return word1
    elif len(word2) > len(word1):
        return word2
    else:
        print("Their length are same")

w1 = input("First Word:")
w2 = input("Second Word:")
result = check_length(w1, w2)

if result:
    print(result)