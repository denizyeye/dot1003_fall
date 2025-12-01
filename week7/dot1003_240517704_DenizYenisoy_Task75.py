score = 0

def start_game():
    global score
    score = 10
    print(f"Game started! Current score: {score}")

def increase_score():
    global score
    score += 5
    print(f"Score increased! Current score: {score}")

def display_score():
    print(f"Final score: {score}")

start_game()
increase_score()
display_score()