from ..assets import shipExplosionImages
from ..utils.animation import Animation
from ..config import shipExplosionScrollPeriod


class ShipExplosion(object):

    def __init__(self, screen, pos):

        self.screen = screen
        self.pos = pos
        self.images = shipExplosionImages

        self.scrollPeriod = shipExplosionScrollPeriod
        self.duration = len(self.images) * self.scrollPeriod

        self.explosion = Animation(self.screen, self.pos, self.images,
                                   self.scrollPeriod, self.duration)

    def update(self, timePassed):
        self.explosion.update(timePassed)

    def blitMe(self):
        self.explosion.blitMe()
