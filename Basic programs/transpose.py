#write a program to find the transpose of matrix
import numpy as np

matrix1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

transposem = np.transpose(matrix1)
print("Given matrix", matrix1)
print("transposed matrix",transposem)