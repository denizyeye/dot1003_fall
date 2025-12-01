def to_two_decimal(numbers):
    new_list = []
    for num in numbers:
        # Format as string with 2 decimal places
        formatted_num = f"{num:.2f}" 
        new_list.append(formatted_num)
    return new_list

my_list = [1.2345, 2.3456, 3.4567, 4.5678]
new_list = to_two_decimal(my_list)
print(new_list)