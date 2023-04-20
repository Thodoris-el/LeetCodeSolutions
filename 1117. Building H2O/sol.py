from threading import Semaphore
class H2O(object):
    def __init__(self):
        self.hy = Semaphore(2)
        self.ox = Semaphore(0)
        pass


    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: method
        :rtype: void
        """
        self.hy.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        if self.hy._Semaphore__value == 0:
            self.ox.release()


    def oxygen(self, releaseOxygen):
        """
        :type releaseOxygen: method
        :rtype: void
        """
        self.ox.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.hy.release()
        self.hy.release()
