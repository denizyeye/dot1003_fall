def tree():
    my_flag = True
    while my_flag:
        try:
            height = int(input("enter a number for tree height: "))
            frame = int(input("enter a number for frame size: "))

            tree_width = 2 * height - 1

            if frame < tree_width:
                print("frame size couldn't be smaller than the tree.")
                continue
            
            my_flag = False
            
        except ValueError:
            print("Please enter a valid number.")
            continue


    print("-" * (frame + 2))
    print("|" + " " * frame + "|")
    
    for i in range(1, height + 1):
        stars = "*" * (2 * i - 1)
        space = frame - len(stars)
        left = space // 2
        right = space - left
        print("|" + " " * left + stars + " " * right + "|")

    
    trunk_width = 3
    trunk_height = 2

    trunk_left_space = (frame - trunk_width) // 2
    trunk_right_space = frame - trunk_width - trunk_left_space

    for k in range(trunk_height):
        trunk_chars = "|" * trunk_width
        print("|" + " " * trunk_left_space + trunk_chars + " " * trunk_right_space + "|")

    print("-" * (frame + 2))

tree()