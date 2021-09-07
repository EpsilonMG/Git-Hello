import numpy as np
matrix1=np.array([[11,10,22],
                  [4,30,50],
                  [30,40,12]])
matrix2=np.array([[1,10,12],
                  [43,7,54],
                  [42,0,1]])
reult=np.array([[0,0,0],
                  [0,0,0],
                  [0,0,0]])

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[j][i]+=matrix1[j][k]*matrix2[k][i]
