#!/usr/bin/python
# Filename : trapezoid.py 

class Shape:
    'Trapzoidal rule for Integration'
    def __init__ (self,f,a,b,n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n
        
    def trapezoidal(self):
        h = float(b-a)/n
        result = 0.5 * f(a) + 0.5*f(b)
        for i in range (1,n):
            result += f(a + i*h)
        result *= h
        return result
    
if __name__ == '__main__': # If the program is not imported then 'dfdf' is printed, and the 'dfdff' is printed.
    print "dfdf"
else: # If the program is imported, print dfdff 
    print "dfdff"
o
