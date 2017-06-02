from pygame.sprite import Sprite
from random import randint, choice
from ..assets import asteroidImage
from ..config import asteroidTranslationSpeed
from ..utils.vec2d import Vec2d


class Asteroid(Sprite):
    """
    Simple asteroid which can collide with the ship and reduce it's health,
    or be destroyed by a bullet or other effect.

    Attributes:
        screen (pygame.Surface): Screen to which the asteroid is drawn to.
        image (pygame.Image): Image of the asteroid.
        rect (pygame.Rect): Bounding box of the asteroid.
        pos (Vec2d): Position of the asteroid.
        direction (Vec2d): Direction of the asteroid.
        asteroidSpeed (float): Asteroid speed.
    """

    def __init__(self, screen):

        Sprite.__init__(self)

        # Asteroid attributes.
        self.screen = screen
        self.image = asteroidImage
        self.rect = None
        self.pos = None
        self.direction = None
        self.asteroidSpeed = asteroidTranslationSpeed

        # Generate starting position and direction vectors.
        self.generatePosition()
        self.generateDirection()

        # Set initial bounding box.
        self.updateRect()

        # Use time alive to know if asteroid is active or not.
        # Cannot only rely if asteroid is on screen.
        self.timeAlive = 0.0

    def generatePosition(self):
        """
        Pick a starting point for the asteroid randomly, either from
        the left, top, right, or bottom of the screen.
        """
        screenWidth, screenHeight = self.screen.get_size()
        delta = 10  # Distance from screen in all four cases.

        staringPositions = ((-delta, randint(0, screenHeight)),  # Left
                            (randint(0, screenWidth), -delta),  # Top
                            (delta, randint(0, screenHeight)),  # Right
                            (randint(0, screenWidth), delta))  # Bottom

        self.pos = Vec2d(choice(staringPositions))

    def generateDirection(self):
        """
        Pick a random point on the screen, and set the asteroid direction
        towards that point.
        """
        screenWidth, screenHeight = self.screen.get_size()
        randX = randint(0, screenWidth)
        randY = randint(0, screenHeight)
        randomPoint = Vec2d(randX, randY)

        # Get angle between asteroid's position and random point.
        angleToRandomPoint = self.pos.get_angle_between(randomPoint)

        self.direction = Vec2d((1, 0))
        self.direction.rotate(angleToRandomPoint)

    def inBounds(self):
        screenWidth, screenHeight = self.screen.get_size()

        return 0 <= self.pos.x and self.pos.x < screenWidth and \
            0 <= self.pos.y and self.pos.y < screenHeight

    def isActive(self):
        return self.inBounds() or self.timeAlive < 1000.0

    def update(self, timePassed):
        self.pos += self.direction * timePassed * self.asteroidSpeed

        self.timeAlive += timePassed

    def updateRect(self):
        imageWidth, imageHeight = self.image.get_size()

        self.rect = self.image.get_rect().move(
            self.pos.x - imageWidth / 2,
            self.pos.y - imageHeight / 2)

    def blitMe(self):
        # First update bounding box.
        self.updateRect()

        # Draw asteroid to screen.
        self.screen.blit(self.image, self.rect)
