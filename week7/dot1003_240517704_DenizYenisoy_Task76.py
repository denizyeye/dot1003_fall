def age_calc():
    my_flag = False
    age = 0
    
    while not my_flag:
        try:
            birth_year = int(input("What is your birthyear? "))
            current_year = 2024
            age = current_year - birth_year
            my_flag = True
        except ValueError:
            print("Invalid Input.")
            
    return age

print(f"You are {age_calc()} years old")