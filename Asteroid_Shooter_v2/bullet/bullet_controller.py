import pygame
import copy

from ..config import timeBetweenBullets, bulletLimit
from ..config import timeCooldownStart, timeBetweenBulletCooldowns
from ..config import timeBetweenBulletSpamBullets
from bullet import Bullet


class BulletController(object):
    """
    Controls whether bullets can be shot or not from a certain ship
    depening on dynamic in-game conditions.

    Each bullet controller is tied to a ship from which the bullets are shot
    from, and the controller contains all these bullets.

    Attributes:
        screen (pygame.Surface): Screen to which child bullets are drawn to.
        ship (Ship): Ship to which current bullet controller is tied to.tied
        bullets (list of Bullet): Child bullets of current controller.
        timeBetweenBullets (float): Minimum time between successive bullets.
        timeSinceLastBullet (float): Time since last bullet shot.
        keyboardInput (bools): State of keyboard keys pressed from last frame.
        bulletSpamCount (int): Number of bullet spam powerups currently active.
    """
    def __init__(self, screen, ship, bulletSound):

        # Bullet controller attributes.
        self.screen = screen
        self.ship = ship
        self.bullets = []
        self.bulletSound = bulletSound
        self.timeBetweenBullets = timeBetweenBullets
        self.timeSinceLastBullet = 0
        self.keyboardInput = None
        self.bulletSpamCount = 0
        self.wideBulletCount = 0

        self.bulletCount = 0
        self.bulletLimit = bulletLimit

        self.timeCooldownStart = timeCooldownStart
        self.timeBetweenBulletCooldowns = timeBetweenBulletCooldowns

        self.timeBetweenBulletSpamBullets = timeBetweenBulletSpamBullets

    def getKeyboardInput(self, keysPressed):
        self.keyboardInput = keysPressed

    def canShoot(self):
        # If bullet spam is active just shoot.
        if self.bulletSpamCount:
            return self.timeSinceLastBullet > self.timeBetweenBulletSpamBullets

        return self.bulletCount < self.bulletLimit and \
            self.timeSinceLastBullet > self.timeBetweenBullets and \
            self.ship.shipHealth > 0

    def shoot(self):
        if self.canShoot():

            # Play bullet sound.
            self.bulletSound.play()

            if not self.bulletSpamCount:
                self.bulletCount += 1

            if not self.wideBulletCount:
                self.spawnBullet()
            else:
                self.spawnWideBullet()

    def spawnBullet(self):
        # Copy ship position and direciton.
        shipPosition = copy.copy(self.ship.pos)
        shipDirection = copy.copy(self.ship.direction)

        # Spawn new bullet with current ship position and direction.
        self.bullets.append(Bullet(self.screen,
                                   shipPosition,
                                   shipDirection))
        self.timeSinceLastBullet = 0

    def spawnWideBullet(self):
        shipDirection = copy.copy(self.ship.direction)

        for angle in [-15.0, 0.0, 15.0]:
            shipPosition = copy.copy(self.ship.pos)

            rotatedDirection = shipDirection.rotated(angle).normalized()

            self.bullets.append(Bullet(self.screen,
                                       shipPosition,
                                       rotatedDirection))
            self.timeSinceLastBullet = 0

    def activateBulletSpam(self):
        self.bulletSpamCount += 1

    def deactivateBulletSpam(self):
        self.bulletSpamCount -= 1

    def activateWideBullet(self):
        self.wideBulletCount += 1

    def deactivateWideBullet(self):
        self.wideBulletCount -= 1

    def maintainBullets(self):
        """
        Delete bullets that are outside the screen area.
        """
        for bullet in self.bullets:
            if not bullet.inBounds():
                self.bullets.remove(bullet)

    def clearBullets(self):
        self.bullets[:] = []

    def updateBulletCooldown(self):

        # Check if cooldown has started.
        if self.timeSinceLastBullet > self.timeCooldownStart:

            # Check if we can remove bullet.
            if self.bulletCount > 0:
                self.bulletCount -= 1
                self.timeSinceLastBullet -= self.timeBetweenBulletCooldowns

    def updateController(self, timePassed):
        self.timeSinceLastBullet += timePassed

        # Check if user tried to shoot.
        if self.keyboardInput[pygame.K_SPACE]:
            self.shoot()

    def update(self, timePassed):
        """
        Update bullet controller and all of it's bullets.
        """
        self.updateController(timePassed)
        self.updateBulletCooldown()

        for bullet in self.bullets:
            bullet.update(timePassed)

        self.maintainBullets()  # Delete bullets off screen.

    def blitBullets(self):
        """
        Draw all child bullets to screen.
        """
        for bullet in self.bullets:
            bullet.blitMe()
