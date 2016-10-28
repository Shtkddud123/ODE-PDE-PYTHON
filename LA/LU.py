import pprint
import scipy
import scipy.linalg  # SciPy Linear Algebra library

## input and output
A = scipy.array([ [7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6] ])
P, L, U = scipy.linalg.lu(A)


print P
print L
print U
