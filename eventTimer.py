class Timer(object):
    def __init__(self, interval, *args, function):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.is_running = False
        self.start() 
        
    def __runTimer(self):
        self.is_run = False
        self.start()
        self.function(*self.args)
        
    def start(self):
        if not self.is_run:
            self._timer = Timer(self.interval, self._runTimer)
            self._timer.start()
            self.is_run = True
    
