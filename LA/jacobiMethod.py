from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot # import specific methods from numpy

def jacobi(A,b,N=25,x=None):
    """ Solves the equation Ax=b via the jacobi iterative method
    In the original LA equation, Ax = b, we divide the A into two 
    diagonal matrices, R and D, where R consists of R_{ij} == A_{ij}/R_{ii} == 0
    and D_{ij} == 0/D_{ii} == A_{ii}.

    The [x1..] vector (or the solution to the matrix) is given by the 
    
    """
    # Create the initial guess if needed
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A
    # and subtract them from A

    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times - implementation of the Jacobi iterative formula 
    for i in range(N):
        x = (b - dot(R,x))/D
    return x


