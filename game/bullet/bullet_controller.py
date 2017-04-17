import pygame
import copy

from ..config import timeBetweenBullets
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
    """
    def __init__(self, screen, ship):

        # Bullet controller attributes.
        self.screen = screen
        self.ship = ship
        self.bullets = []
        self.timeBetweenBullets = timeBetweenBullets
        self.timeSinceLastBullet = 0
        self.keyboardInput = None

    def getKeyboardInput(self, keysPressed):
        self.keyboardInput = keysPressed

    def canShoot(self):
        return self.timeSinceLastBullet >= self.timeBetweenBullets

    def shoot(self):
        if self.canShoot():
            # Copy ship position and direciton.
            shipPosition = copy.copy(self.ship.pos)
            shipDirection = copy.copy(self.ship.direction)

            self.bullets.append(Bullet(self.screen,
                                       shipPosition,
                                       shipDirection))
            self.timeSinceLastBullet = 0

    def maintainBullets(self):
        """
        Delete bullets that are outside the screen area.
        """
        for bullet in self.bullets:
            if not bullet.inBounds():
                self.bullets.remove(bullet)

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

        for bullet in self.bullets:
            bullet.update(timePassed)

        self.maintainBullets()  # Delete bullets off screen.

    def blitBullets(self):
        """
        Draw all child bullets to screen.
        """
        for bullet in self.bullets:
            bullet.blitMe()
