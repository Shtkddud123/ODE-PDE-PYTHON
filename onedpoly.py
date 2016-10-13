import numpy as np
import scipy

p = scipy.poly1d([3,4,5])
print p

if __name__ == '__main__':
    print "This program is run in it's own source file"
else: 
    print "This progam is imported"


