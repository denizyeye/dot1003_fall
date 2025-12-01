total = 0
counter = 0
even_counter = 0
odd_counter = 0

my_flag = True

print("malculator v0.1")
print("")
print("enter 0 to exit")
print("")

while my_flag:
    number = int(input("enter a number: "))

    if number == 0:
        my_flag = False
    else:
        counter = counter + 1
        total = total + number

        if number % 2 == 0:
            even_counter = even_counter + 1
        else:
            odd_counter = odd_counter + 1

if counter > 0:
    average = total / counter
else:
    average = 0

print("Total Number:", counter)
print("Sum:", total)
print("Mean:", average)
print("Odd:", odd_counter, "Even:", even_counter)