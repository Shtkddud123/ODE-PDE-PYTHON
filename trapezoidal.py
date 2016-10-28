#!/usr/bin/python
# Filename : trapezoid.py 
from math import exp 

class Shape:
    'Trapzoidal rule for Integration'
    def __init__ (self,f,a,b,n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n
        
    def trapezoidal(self):
        h = float(self.b- self.a)/self.n
        result = 0.5 * f(self.a) + 0.5*f(self.b)
        for i in range (1,self.n):
            result += f(self.a + i*h)
        result *= h
        return result

class AnonymousFunction:
    'Example lambda function - or what is called, an anonymous function'
    def __init__(self,t):
        self.t = t 
    def lambdaFunction(self):
        anonFunction = lambda tt: 3*(tt**2)*exp(tt**3)
       # print anonFunction
        return anonFunction

if __name__ == '__main__': # If the program is not imported then 'dfdf' is printed, and the 'dfdff' is printed.
    print "This module is not imported from another file"
else: # If the program is imported, print dfdff 
    print "This module is imported from a file"
