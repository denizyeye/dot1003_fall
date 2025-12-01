my_flag = True
password = input("Enter your password: ")

while my_flag:
    password2 = input("Enter again: ")
    if password == password2:
        print("Your password matches and account created successfully")
        my_flag = False
    else:
        print("They are not same.")
        