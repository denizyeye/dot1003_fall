x = int(input("Please enter a number:"))
my_flag = True

while my_flag:
    try:
        y = int(input("Please enter divider:"))
        print(f"{x} divided by {y} is {x/y}")
        my_flag = False
        
    except ZeroDivisionError:
        print("You can't enter 0 as divider")
        
    except ValueError:
        print("Invalid Value")
        
    except:
        print("Some kind of error occured")