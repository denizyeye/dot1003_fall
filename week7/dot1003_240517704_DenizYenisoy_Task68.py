def coordinator(x, y):
    return (x, y)

my_coordinates = {}

my_coordinates[coordinator(0, 0)] = "Home"
my_coordinates[coordinator(1, 1)] = "Work"
my_coordinates[coordinator(-1, -1)] = "School"

for k, v in my_coordinates.items():
    print(f"position: {k} name: {v}")