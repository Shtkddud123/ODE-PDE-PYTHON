"""
__init__ - it's the way that we can define the initialization behaviour of an objectt 

x = someclass(), it is not the first thing that is called. It's actually a method called __new__ 
which actually creates the instance, then passes any arguments at creation on to the initalizer 

__del__  - if __new__ and __init__ formed the constructor of the object, __del__ is the destructor 

"""
from os.path import join

class FileObject:
    '''Wrapper for file objects to make sure the file gets closed on deletion'''

    def __init__(self,filepath='~', filename='sample.txt'):
        # open a file filename in filepath in read and write mode
        self.file = open(join(filepath,filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file 
