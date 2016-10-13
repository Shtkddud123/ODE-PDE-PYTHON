import threading
import time
import logging

#

from threading import Thread

# Template
from string import Template

logging.basicConfig(level = logging.DEBUG,
                   format = '[%(levelname)s] (%(threadName)-10s) %(message)s',
                   )
def worker():
    """ Thread worker function"""
    print 'Worker'
    return

def timer(name, delay, repeat):
    print "Timer: " + name + " Started"
    while repeat > 0:
        time.sleep(delay)
        print name + ": " + str(time.ctime(time.time()))
        repeat -= 1
    print "Timer: " + name + " Completed"

def randomPrinting(a, b):
    print a + b 


def NewWorker():
    logging.debug('Starting')
   # print threading.currentThread().getName(), 'Starting' # This has a default value at the moment 
    time.sleep(10)
    logging.debug('Exiting')
    #print threading.currentThread().getName(), 'Exiting'

def my_service():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(3)
    print threading.currentThread().getName(), 'Exiting'
    
def Main():
    t1 = Thread(target=randomPrinting, args =("Timer1",1,5))
    t2 = Thread(target=randomPrinting, args = ("Timer2", 2, 5))
    t1.start()
    t2.start()
    
    for i in range (10):
        t3 = Thread(target=randomPrinting, args =(i,i))
        t4 = Thread(target=randomPrinting, args = (i,i))        
        t3.start()
        t4.start()


    t5 = Thread(target = NewWorker) # default thread
    t5.start()
    
    print "Main Complete"
    
#threads = []
#for i in range(5):
 #   t = threading.Thread(target=worker)
  #  threads.append(t)
   # t.start()
   
if __name__ == '__main__':
    print "Running from source file" # Only prints out when not imported 
    Main()
    
