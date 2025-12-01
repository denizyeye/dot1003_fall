game_table = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
user_inputs = []

def coordinator(x, y):
    return (x, y)

is_running = True

while is_running:
    command = input("please type new or exit: ")
    
    if command == "exit":
        is_running = False
    elif command == "new":
        x = int(input("please enter x: "))
        y = int(input("please enter y: "))
        user_inputs.append(coordinator(x, y))

for coord in user_inputs:
    x, y = coord
    if 0 <= x < 3 and 0 <= y < 3:
        game_table[x][y] = "*"

for row in game_table:
    print(row)