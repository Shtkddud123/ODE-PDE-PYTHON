import threading
import time
import onedpoly

class AsyncWrite(threading.Thread):
    'Define the initializer'
    def __init__(self,text,out):
        threading.Thread.__init__(self) # Inherit thread functions
        self.text = text # text 
        self.out = out # out 

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + '\n')
        f.close()
        time.sleep(2) ## Delay printing out the 
        print "Finished Background file write to " + self.out


def Main():
    message = raw_input("Enter a string to store:")
    background = AsyncWrite(message, "out.txt")
    background.start()
#    print background.activeCount()
    print "The program can continue to run while it writes in another thread"
    print 100 + 400

    print onedpoly.p
    
    background.join()
    print "waited until thread was complete"

if __name__ == '__main__':
    Main()
