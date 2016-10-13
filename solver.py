from PyDSTool import *

class odeSystem:
    """Create an initial ODE system
    In this case, we are creating one for the
    m(x'') = - kx  
    In this case, we need to define the initial conditions for the x/y values and the intial values 
    of m and k which represent the mass and spring constant respectively.
 """
    def __init__(self,x,y,k,m):
        self.name = 'SHM'
        self.x = x # x value 
        self.y = y # y value
        self.k = k # spring constant 
        self.m = m # mass 
        self.ics = {'x':self.x, 'y':self.y} # initial conditions for the x and y values
        self.pars= {'k':self.k, 'm':self.m} # initial conditions for the parameters

    def function(self,x_rhs,y_rhs): # Representing the system of equations
        self.x_rhs = x_rhs
        self.y_rhs = y_rhs
        self.varspecs = {'x':self.x_rhs, 'y':self.y_rhs}
        self.tdata = [0,20]
        
        
