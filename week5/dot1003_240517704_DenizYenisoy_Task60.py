def finder(matrix, item):
    my_flag = False
    row_idx = 0
    
    for row in matrix:
        col_idx = 0
        for element in row:
            if element == item:
                print(f"find at row: {row_idx} column: {col_idx}")
                my_flag = True
            col_idx += 1
        row_idx += 1
        
    return my_flag

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = int(input("item to search:"))

for row in my_matrix:
    print(row)

print(finder(my_matrix, element))