# By Hossam Ibrahim:

vec1 = [1, 3, 55, 66, 3, 66, 3, 9]     # mean, median, mode and variance

# 1) My Functions (mean, median, mode ) :

# Mean:
def my_mean(vec1):
    m1 = 0
    for i in vec1:  m1 += i
    mean1 = m1 / len(vec1)

    print(mean1)
    return mean1


# Median:
def my_median(vec1):
    vec1.sort()
    if len(vec1) % 2 == 0:
        mdn2 = vec1[len(vec1) // 2]
        mdn3 = vec1[len(vec1) // 2 - 1]
        median1 = (mdn2 + mdn3) / 2      # median
    else:
        median1 = vec1[len(vec1) // 2]
    print(median1)
    return median1


# Mode:
def my_mode(vec1):
    vec1.sort()
    counter1 = {}

    for i in range(len(vec1)):
        counter1[vec1[i]] = 0  # first key
        for elem in vec1:
            if elem == vec1[i]:
                counter1[vec1[i]] += 1

    mode1 = [k for k, v in counter1.items() if v == max(list(counter1.values()))]  # mode is a list

    print(mode1[0])
    return mode1



# 2) Using Libraries  (for mean, median, mode & variance) :

# mean:
import numpy as np
mean2 = np.mean(vec1)
print(mean2)


# median:
import numpy as np
mdn = np.median(vec1)


# mode:
from collections import counter
c= counter(vec1)
print(c)
print(c.most_common())
print( c.most_common()[0] )    # first tuple
print( c.most_common()[0][0] ) # key


# Vairance:
import numpy as np
variance2 = np.var(vec1)
print(variance2)



# 3) Matrix multiplication:

matrix1 =  [ [1 2 3],                   # multiply matrices
             [4 5 6],
             [6 7 8] ]

matrix2 = [ [1,2,3],
            [4,5,6],
            [6,7,8] ]

def multiply_matrices(matrix1, matrix2):
    result = [ [0,0,0], [0,0,0], [0,0,0] ]

    for j in range(len (matrix1)):
        for i in range(len (matrix2[0])):
            for k in range (len (matrix2)):
                result [j][i] += matrix1 [j][k] * matrix2 [k][i]
    print('result',result)
    return result


def matrices_dot_product(matrix1, matrix2):
    import numpy as np
    result = np.dot(matrix1, matrix2)
    print('result matrix: ', result)
    return result




# main() :
my_mean(vec1)
my_median(vec1)
my_mode(vec1)

# main() :
multiply_matrices(matrix1, matrix2)
matrices_dot_product(matrix1, matrix2)