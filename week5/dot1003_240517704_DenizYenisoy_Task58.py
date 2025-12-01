game_list = []
my_flag = True
game = ""

while my_flag:
    game = input("Enter a game:")
    if game.lower() == "exit":
        my_flag = False
    else:
        game_list.append(game)

def anarya(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

print(game_list)
print(anarya(game_list))
