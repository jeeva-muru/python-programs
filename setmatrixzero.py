
def setzero(matrix):
    if not matrix:
        return matrix
    row = len(matrix)
    col = len(matrix[0])
   
    row_num =0
    col_num=0
    zero = []
    for i in range(0, row):
        for j in range(0, col):
            if matrix[i][j] == 0:
                row_num =i
                col_num =j
                zero.append([i,j])
    print(zero)
   
    for j in range(0, len(zero)):
        row_num = zero[j][0]
        col_num = zero[j][1]
        print(row_num, col_num)
        for r in range(0, row):
            matrix[r][col_num] = 0
            matrix[row_num][r] = 0

    return matrix            

#main
# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setzero(matrix)
print(matrix)    

