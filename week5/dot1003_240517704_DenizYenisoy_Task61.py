def sum_of_row(matrix, row_no):
    if 0 <= row_no < len(matrix):
        return sum(matrix[row_no])
    else:
        return 0

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target_row = int(input("row no:"))

for row in my_matrix:
    print(row)

print(sum_of_row(my_matrix, target_row))