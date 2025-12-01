def sum_of_column(matrix, col_no):
    total = 0
    for row in matrix:
        if 0 <= col_no < len(row):
            total += row[col_no]
    return total

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target_col = int(input("column no:"))

for row in my_matrix:
    print(row)

print(sum_of_column(my_matrix, target_col))