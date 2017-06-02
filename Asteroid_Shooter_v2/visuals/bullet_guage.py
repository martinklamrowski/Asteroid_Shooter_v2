import pygame
from ..colors import red


class BulletGuage(object):

    def __init__(self, screen, bulletController):

        self.screen = screen
        self.bulletController = bulletController

        # Set bounding box of bullet guage.
        screenWidth, screenHeight = self.screen.get_size()
        self.rect = [screenWidth - 100, screenHeight - 20, 80, 10]

    def blitMe(self):

        bulletCount = self.bulletController.bulletCount
        bulletLimit = self.bulletController.bulletLimit

        percentageFilled = bulletCount / float(bulletLimit)

        # Only draw if there are bullets on cooldown.
        if percentageFilled > 0.0:
            partFilledRect = self.rect[:]
            partFilledRect[2] = partFilledRect[2] * percentageFilled

            pygame.draw.rect(self.screen, red, partFilledRect)
