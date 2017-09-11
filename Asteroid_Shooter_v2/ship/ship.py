import pygame

from pygame.sprite import Sprite
from ..assets import shipImage, transparentShipImage
from ..utils.vec2d import Vec2d
from ..utils.timer import Timer
from ..config import keyToTranslationVector, keyToRotationAngle, shipHealth
from ..config import invincibilityDuration


class Ship(Sprite):
    """
    Class for player controlled ship.

    Ship can move up, down, left, right and rotate cloclwise and
    counterclockwise.

    Attributes:
        screen (pygame.Surface): Screen to which the ship is drawn to.
        image (pygame.Image): Original image of the ship.
        invincibleImage (pygame.Image): Image when ship is invincible.
        currentImage (pygame.Image): Image we are currently drawing.
        rect (pygame.Rect): Bounding box of the ship.
        pos (Vec2d): Current position of the ship.
        shipHealth (int): Lives ship currently has left.
        direction (Vec2d): Normalized direction vector of the ship.
        keyboardInput (bools): State of keyboard keys pressed from last frame.
        isInvincible (bool): Whether ship is invincible or not.
        invincibilityTimer (Timer): Timer for when to stop invincibility.
    """

    def __init__(self, screen, position):

        Sprite.__init__(self)

        # Ship attributes
        self.screen = screen
        self.image = shipImage
        self.invincibleImage = transparentShipImage
        self.currentImage = None
        self.rect = None
        self.pos = position
        self.shipHealth = shipHealth
        self.direction = Vec2d((1, 0))  # Initially point ship right.
        self.keyboardInput = None

        self.isInvincible = False
        self.invincibilityTimer = None

    def getKeyboardInput(self, keysPressed):
        """
        Save keyboard input for update later when context of time
        passed between frames is given.
        """
        self.keyboardInput = keysPressed

    def shipCollided(self):
        """
        Decreases the ship's health by one.
        If the ship is still alive, ship starts invincibility and the function
        returns True meaning the ship is still alive.
        Otherwise returns False meaning the ship is dead.
        """
        self.shipHealth -= 1

        if self.shipHealth > 0:
            self.startInvincibilty()
            return True
        else:
            return False

    def keepInBounds(self):
        """
        Keep ship in bounds of the screen.
        """
        screenWidth, screenHeight = self.screen.get_size()

        self.pos.x = max(0, self.pos.x)
        self.pos.x = min(screenWidth, self.pos.x)

        self.pos.y = max(0, self.pos.y)
        self.pos.y = min(screenHeight, self.pos.y)

    def update(self, timePassed):
        """
        Update ship position and direction based on keyboard input.
        """
        # Handle translation updates.
        for key, translationVector in keyToTranslationVector.items():
            if self.keyboardInput[key]:  # If key has been pressed.
                self.pos += timePassed * translationVector

        # Handle rotation updates.
        for key, rotationAngle in keyToRotationAngle.items():
            if self.keyboardInput[key]:
                self.direction.rotate(rotationAngle * timePassed)

        # Update invincibilty state.
        self.updateInvincibility(timePassed)

        # Keep ship in bounds of screen.
        self.keepInBounds()

    def startInvincibilty(self):
        self.isInvincible = True
        self.invincibilityTimer = Timer(invincibilityDuration,
                                        self.stopInvincibility, callLimit=1)

    def stopInvincibility(self):
        self.isInvincible = False
        self.invincibilityTimer = None

    def updateInvincibility(self, timePassed):
        if self.isInvincible:
            self.invincibilityTimer.update(timePassed)

    def updateImage(self):

        curImage = self.image
        if self.isInvincible:
            curImage = self.invincibleImage

        self.currentImage = pygame.transform.rotate(
            curImage, -self.direction.angle)

    def updateRect(self):
        imageWidth, imageHeight = self.currentImage.get_size()

        self.rect = self.currentImage.get_rect().move(
            self.pos.x - imageWidth / 2,
            self.pos.y - imageHeight / 2)

    def blitMe(self):
        # Update new ship image after rotating.
        self.updateImage()

        # First update bounding box.
        self.updateRect()

        # Draw ship to screen.
        self.screen.blit(self.currentImage, self.rect)
