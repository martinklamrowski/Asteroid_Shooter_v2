import copy

from ..assets import heartImage
from ..config import healthBarMargin
from ..utils.vec2d import Vec2d


class HealthBar(object):
    """
    Health bar shows how many lives the player's ship still has by drawing an
    'object' for life left.

    Attributes:
        screen (pygame.Surface): Screen to which the ship is drawn to.
        ship (Ship): The ship which health we are following.
        image (pygame.Image): Image a 'life'.
        startingPos ((int,int)): Where the first life should be placed.
        margin (int): Distance in pixels between two adjacent life images.
    """

    def __init__(self, screen, ship):

        self.screen = screen
        self.ship = ship
        self.image = heartImage

        screenWidth, screenHeight = self.screen.get_size()
        self.startingPos = Vec2d(20, screenHeight - 40)

        self.margin = healthBarMargin

    def blitLifeAtPosition(self, pos):
        # Get bounding box for image at that position.
        imageWidth, imageHeight = self.image.get_size()

        rect = self.image.get_rect().move(
            pos.x - imageWidth / 2,
            pos.y - imageHeight / 2)

        # Draw life.
        self.screen.blit(self.image, rect)

    def blitMe(self):

        currentShipHealth = self.ship.shipHealth

        currentPos = copy.copy(self.startingPos)

        # Draw each life individually, and shift drawing position right.
        for life in range(currentShipHealth):
            # Draw life.
            self.blitLifeAtPosition(currentPos)

            # Shift position right by image width and margin.
            imageWidth, _ = self.image.get_size()
            currentPos.x += imageWidth + self.margin
