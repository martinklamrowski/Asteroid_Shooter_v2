from ..utils.collisions import doCollide
from ..utils.vec2d import Vec2d
from bulletspam import BulletSpamPowerup
from wide_bullet import WideBulletPowerup
#from deflector_shield import DeflectorShieldPowerup

import random


class PowerupController(object):
    """
    Class that controlls spawning, updating, and drawing of powerups.

    Attributes:
        screen (pygame.Surface): Screen to which asteroids will be drawn to.
        ship (Ship): Ship with which powerups can collide with.
        powerups (list of Powerups): Child powerups of controller.
    """

    def __init__(self, screen, ship, bulletController):

        self.screen = screen
        self.ship = ship
        self.bulletController = bulletController
        self.powerups = []

    def handleCollisionsWithShip(self):
        """
        Check if any alive but not active powerups collide with the ship.
        If some do, activate them.
        """
        for powerup in self.powerups:
            if not powerup.active:
                if doCollide(self.ship, powerup):
                    powerup.activatePowerup()

    def spawnBulletSpamPowerup(self):

        powerupPos = self.getRandomPositionOnScreen()

        self.powerups.append(BulletSpamPowerup(self.screen, powerupPos,
                                               self.bulletController))

    def spawnWideBulletPowerup(self):
        powerupPos = self.getRandomPositionOnScreen()

        self.powerups.append(WideBulletPowerup(self.screen, powerupPos,
                                               self.bulletController))
    """
    def deflectorShieldPowerup(self):
        powerupPos = self.
        
        self.powerups.append(DeflectorShieldPowerup(self.screen, powerupPos))
    """
    def spawnRandomPowerup(self):

        availablePowerups = [self.spawnBulletSpamPowerup,
                             self.spawnWideBulletPowerup]

        randomPowerup = random.choice(availablePowerups)

        randomPowerup()

    def getRandomPositionOnScreen(self):
        """
        Create random position on the screen.
        """
        screenWidth, screenHeight = self.screen.get_size()
        delta = 10

        return Vec2d((random.randint(0 + delta, screenWidth - delta),
                      random.randint(0 + delta, screenHeight - delta)))

    def maintainPowerups(self):
        """
        Delete powerups that are no longer alive.
        """
        for powerup in self.powerups:
            if not powerup.alive:
                self.powerups.remove(powerup)

    def clearPowerups(self):
        self.powerups[:] = []

    def updatePowerups(self, timePassed):
        for powerup in self.powerups:
            powerup.update(timePassed)

    def drawPowerups(self):
        for powerup in self.powerups:
            powerup.blitMe()
