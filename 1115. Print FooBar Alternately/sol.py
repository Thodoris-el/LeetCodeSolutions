from threading import Event
class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.event_bar = threading.Event()
        self.event_foo = threading.Event()


    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            printFoo()
            self.event_bar.set()
            self.event_foo.wait()
            self.event_foo.clear()


    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.event_bar.wait()
            self.event_bar.clear()
            printBar()
            self.event_foo.set()
