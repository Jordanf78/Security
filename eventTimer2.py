import _thread
import threading

class Timer(threading._Timer):
    
    def __init__(self, *args, **kwargs):
        threading._Timer.__init__(self, *args, **kwargs)
        self.setDaemon(True)

    def run(self):
        while True:
            self.finished.clear()
            self.finished.wait(self.interval)
            if not self.finished.isSet():
                self.function(*self.args, **self.kwargs)
            else:
                return
            self.finished.set()

class Manager(object):

    ops = []

    def add_Timer(self, Timer, interval, args=[], kwargs={}):
        op = Timer(interval, Timer, args, kwargs)
        self.ops.append(op)
        _thread.start_new_thread(op.run, ())

    def stop(self):
        for op in self.ops:
            op.cancel()
        self._event.set()

if __name__ == '__main__':
    
    import time

    def hello():
        print ("Hello World!")

    timer = Manager()
    timer.add_Timer(hello, 10)

    while True:
        time.sleep(.1)
