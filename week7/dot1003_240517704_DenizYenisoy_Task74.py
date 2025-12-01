def ask_name():
    my_ans = input("Please enter a character from Lord of the Rings: ")
    return my_ans

def ask_age(name):
    my_ans = int(input(f"How old is {name}: "))
    return my_ans

real_age = 55000 
name = ask_name()

question = f"Here is the questions about {name}"
print(question)

user_guess = ask_age(name)

if real_age == user_guess:
    my_ans = "You're Right"
    print(my_ans)
else:
    print("Nope")