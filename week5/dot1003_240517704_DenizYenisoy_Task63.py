def tripler(original_list):
    new_list = []
    for num in original_list:
        new_list.append(num * 3)
    return new_list

my_lucky_numbers = [4, 8, 15, 16, 23, 42]
tripled_numbers = tripler(my_lucky_numbers)

print(f"My Lucky Numbers: {my_lucky_numbers}")
print(f"Tripled Numbers: {tripled_numbers}")