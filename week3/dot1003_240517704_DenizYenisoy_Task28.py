number = int(input("Please enter a number:"))
my_flag = True

while my_flag:
    if number == 0:
        print("kaboom")
        my_flag = False
    else:
        print(number)
        number = number - 1