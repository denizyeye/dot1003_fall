user_input = input("Your Input:")

target_width = 17
padding_needed = target_width - len(user_input)

left_pad = ">" * (padding_needed // 2 + padding_needed % 2)
right_pad = "<" * (padding_needed // 2)

print(f"{left_pad}{user_input}{right_pad}|")