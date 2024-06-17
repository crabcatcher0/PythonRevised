row, col = 3, 3
two_dim_list = [[0 for _ in range(col)] for _ in range(row)]
print(two_dim_list)


n = 5
table = [i*n for i in range(1, 11)]
print(table)
#output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

table_of_table = [[i*n for i in range(1, 11)] for n in range(1, 6)]
print(table_of_table)
#output:
#[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
#[3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
#[4, 8, 12, 16, 20, 24, 28, 32, 36, 40], 
#[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]]