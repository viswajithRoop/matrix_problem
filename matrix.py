from typing import List
def matrix(rows,cols):
    # matrix: List[List[int]]
    new_matrix = []
    for i in range(rows):
        new_row = []
        k = i+i
        for j in range(cols):
            new_row.append(k)
            k += 3
        # print(new_row)
        new_matrix.append(new_row)
    new_matrix[0][0]=1
    new_matrix[-1][-1]=rows*cols
    return new_matrix



def matrix_diagonal(rows,cols):
    new_matrix = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(0)
        new_matrix.append(new_row)
    num = 1
    for k in range(rows+cols-1):
        for i in range(rows):
            for j in range(cols):
                if i+j == k and i == j:
                    new_matrix[i][j]=num
                    num = num+1
                elif i+j == k and i>j:
                    new_matrix[i][j]=num
                    num = num+1
                    
                elif i+j ==k and j>i:   
                    new_matrix[j][i]=num
                    num = num+1
    
    return new_matrix


print(matrix(3,3))
print(matrix(3,4))
# print(matrix_diagonal(4,4))
