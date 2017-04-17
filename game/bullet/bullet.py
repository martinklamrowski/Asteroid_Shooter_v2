from pygame.sprite import Sprite
from ..assets import bulletImage
from ..config import bulletTranslationSpeed


class Bullet(Sprite):
    """
    Bullet object that the ship can shoot to destroy asteroids.

    Attributes:
        screen (pygame.Surface): Screen to which bullet will be drawn to.
        image (pygame.Image): Image of the bullet.
        rect (pygame.Rect): Bounding box of the bullet.
        pos (Vec2d): Current position of the bullet.
        direction (Vec2d): Direction of the bullet.
        bulletSpeed (float): Speed of the bullet.
    """

    def __init__(self, screen, position, direction):

        Sprite.__init__(self)

        # Bullet attributes.
        self.screen = screen
        self.image = bulletImage
        self.rect = None
        self.pos = position
        self.direction = direction
        self.bulletSpeed = bulletTranslationSpeed

    def update(self, timePassed):
        distanceTravelled = timePassed * self.bulletSpeed
        self.pos += self.direction * distanceTravelled

    def updateRect(self):
        imageWidth, imageHeight = self.image.get_size()

        self.rect = self.image.get_rect().move(
            self.pos.x - imageWidth / 2,
            self.pos.y - imageHeight / 2)

    def blitMe(self):
        # First update bounding box.
        self.updateRect()

        # Draw bullet to screen.
        self.screen.blit(self.image, self.rect)
