number = 3
my_flag = True
main_password = "314159"


while my_flag:
    password = input("Password:")
    number = number - 1

    if number == 0:
        print("Incorrect Password. Exterminate...")
        my_flag = False
    elif password == main_password:
        print("welcome")
        my_flag = False
    