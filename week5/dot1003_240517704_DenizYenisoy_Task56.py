def clear_vowels(text):
    vowels = "aeiouAEIOU"
    new_string = ""
    for char in text:
        if char not in vowels:
            new_string += char
    return new_string

menu_button = "new game"
print(clear_vowels(menu_button))