def new_game():
    name = input("game name: ")
    try:
        year = int(input("release year: "))
    except ValueError:
        raise ValueError("Year must be a number")

    if len(name) == 0:
        raise ValueError("empty name")
    if len(name) > 40:
        raise ValueError("longer than 40char name")
    if year < 0:
        raise ValueError("negative release date")
    if year > 2024:
        raise ValueError("release date greater than 2024")
        
    return (name, year)

game_list = []
my_flag = True

while my_flag:
    user_command = input("add or exit: ")
    
    if user_command == "exit":
        my_flag = False
    elif user_command == "add":
        try:
            game_tuple = new_game()
            game_list.append(game_tuple)
        except ValueError as e:
            print(f"Error: {e}")

for game in game_list:
    print(f"Name: {game[0]}, Year: {game[1]}")