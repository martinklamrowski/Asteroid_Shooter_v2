from ..utils.timer import Timer
from ..assets import wideBulletImage
from ..config import wideBulletTimeAlive, wideBulletTimeActive


class WideBulletPowerup():

    def __init__(self, screen, pos, bulletController):

        self.screen = screen
        self.image = wideBulletImage
        self.rect = None
        self.pos = pos
        self.bulletController = bulletController
        self.alive = 1
        self.active = 0

        self.timers = []

        # Add timer for how long powerup is alive.
        self.timers.append(Timer(wideBulletTimeAlive, self.killPowerup,
                                 callLimit=1))

        # Update initial bounding box.
        self.updateRect()

    def activatePowerup(self):
        # Mark powerup as active.
        self.active = 1

        # Activate wide bullet through bullet controller.
        self.bulletController.activateWideBullet()

        self.timers[:] = []
        self.timers.append(Timer(wideBulletTimeActive, self.deactivatePowerup,
                                 callLimit=1))

    def deactivatePowerup(self):
        # Deactivate wide bullet through bullet controller.
        self.bulletController.deactivateWideBullet()
        self.active = 0
        self.alive = 0

    def killPowerup(self):
        if self.active:
            self.deactivatePowerup()

        self.alive = 0

    def update(self, timePassed):
        for timer in self.timers:
            timer.update(timePassed)

    def updateRect(self):
        imageWidth, imageHeight = self.image.get_size()

        self.rect = self.image.get_rect().move(
            self.pos.x - imageWidth / 2,
            self.pos.y - imageHeight / 2)

    def blitMe(self):
        # Draw only if alive and not activated yet.
        if self.alive and not self.active:
            # First update bounding box.
            self.updateRect()

            # Draw asteroid to screen.
            self.screen.blit(self.image, self.rect)
