import numpy as np

def matrix_multiply(mtrx1,mtrx2):
    """
    2_D Arrays multiplication function. Given 2 arrays
    """
    res_size=(len(mtrx1),len(mtrx2[0]))
    result=np.zeros(res_size)
    for row in range(len(mtrx1)):
        for col in range(len(mtrx2[0])):
            for col_row in range(len(mtrx2)):
                result[row][col]+=mtrx1[row][col_row]*mtrx2[col_row][col]
    return result

mtrx_a = np.array([[1,2,3],[4,5,6]])
mtrx_b = np.array([[3,5],[9,1],[2,2]])
print(f'{mtrx_a}.\n{mtrx_b}=\n{matrix_multiply(mtrx_a,mtrx_b)}')