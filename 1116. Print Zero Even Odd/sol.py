from threading import Semaphore
class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.sem = [Semaphore(1), Semaphore(0),Semaphore(0)]
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1,self.n+1):
            self.sem[0].acquire()
            printNumber(0)
            self.sem[i % 2 + 1].release()
        
        
        
    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(2, self.n+1, 2):
            self.sem[1].acquire()
            printNumber(i)
            self.sem[0].release()
        
        
        
    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1,self.n+1,2):
            self.sem[2].acquire()
            printNumber(i)
            self.sem[0].release()
