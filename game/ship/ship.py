import pygame

from pygame.sprite import Sprite
from ..assets import shipImage
from ..utils.vec2d import Vec2d
from ..config import keyToTranslationVector, keyToRotationAngle


class Ship(Sprite):
    """
    Class for player controlled ship.

    Ship can move up, down, left, right and rotate cloclwise and
    counterclockwise.

    Attributes:
        screen (pygame.Surface): Screen to which the ship is drawn to.
        image (pygame.Image): Image of the ship.
        rect (pygame.Rect): Bounding box of the ship.
        pos (Vec2d): Current position of the ship.
        diretion (Vec2d): Normalized direction vector of the ship.
        keyboardInput (bools): State of keyboard keys pressed from last frame.
    """

    def __init__(self, screen, position):

        Sprite.__init__(self)

        # Ship attributes
        self.screen = screen
        self.image = shipImage
        self.rect = None
        self.pos = position
        self.direction = Vec2d((1, 0))  # Initially point ship right.
        self.keyboardInput = None

        # Because the ship image rotates, we need to keep the original
        # and update a copy that is rotated.
        self.currentImage = self.image

    def getKeyboardInput(self, keysPressed):
        """
        Save keyboard input for update later when context of time
        passed between frames is given.
        """
        self.keyboardInput = keysPressed

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

        # Update new ship image after rotating.
        self.updateImage()

    def updateImage(self):
        self.currentImage = pygame.transform.rotate(
            self.image, -self.direction.angle)

    def updateRect(self):
        imageWidth, imageHeight = self.currentImage.get_size()

        self.rect = self.currentImage.get_rect().move(
            self.pos.x - imageWidth / 2,
            self.pos.y - imageHeight / 2)

    def blitMe(self):
        # First update bounding box.
        self.updateRect()

        # Draw ship to screen.
        self.screen.blit(self.currentImage, self.rect)
