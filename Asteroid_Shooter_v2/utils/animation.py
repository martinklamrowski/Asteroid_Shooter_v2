from timer import Timer


class Animation(object):

    def __init__(self, screen, pos, images, scrollPeriod, duration=-1):

        self.screen = screen
        self.pos = pos
        self.rect = None
        self.images = images
        self.imageIndex = 0
        self.scrollPeriod = scrollPeriod
        self.duration = 0
        self.active = True

        self.timers = []

        # Add scroll timer for when to advance to next image.
        self.timers.append(Timer(scrollPeriod, self.advanceImage))

        # Add timer to deactivate animation. If needed.
        if self.duration >= 0:
            self.timers.append(Timer(duration, self.deactivate, callLimit=1))

    def update(self, timePassed):
        if self.active:
            for timer in self.timers:
                timer.update(timePassed)

    def blitMe(self):
        if self.active:
            self.updateRect()
            self.screen.blit(self.images[self.imageIndex], self.rect)

    def updateRect(self):
        imageWidth, imageHeight = self.images[self.imageIndex].get_size()

        self.rect = self.images[self.imageIndex].get_rect().move(
            self.pos.x - imageWidth / 2,
            self.pos.y - imageHeight / 2)

    def advanceImage(self):
        self.imageIndex = (self.imageIndex + 1) % len(self.images)

    def deactivate(self):
        self.active = False
