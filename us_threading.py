#!/usr/bin/python
import thread
import time

def worker():
    """thread worker function"""
    print 'Worker'
    return

# Define a function for the thread

def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
    print "%s: %s" %(threadName, time.ctime(time.time()))

        
try:
    thread.start_new_thread(print_time, ("Thread-1", 2, ) )
    thread.start_new_thread(print_time, ("Thread-2", 4, ))
except: # Any errors - throw an exception with the following message:
    print "Error: unable to start thread"

while 1:
    pass


#try:
#    thread.start_new_thread(worker)
#    thread.start_new_thread(worker)
#except: # Any errors - throw an exception with the following message:
#    print "Error: unable to start thread"
#while 1:
#    pass

        
if __name__ == '__main__':
    print "This program is run in it's own source file"
else: 
    print "This progam is imported"
