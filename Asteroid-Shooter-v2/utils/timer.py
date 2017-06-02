class Timer(object):

    def __init__(self, interval, callback, startTime=0.0, callLimit=-1):

        self.interval = interval
        self.callback = callback
        self.startTime = startTime
        self.callLimit = callLimit
        self.time = 0
        self.calls = 0
        self.active = True

    def isActive(self):
        return self.active

    def update(self, time_passed):
        if not self.active:
            return

        self.time += time_passed

        if self.time >= self.startTime + self.interval:
            self.time -= self.interval
            self.calls += 1
            self.callback()

            if self.callLimit > -1 and self.calls >= self.callLimit:
                self.active = False
