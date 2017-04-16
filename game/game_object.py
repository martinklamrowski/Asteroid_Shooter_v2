from pygame.sprite import Sprite


class GameObject(Sprite):
    """
    Abstract class for all drawable game objects.

    Attributes:
        screen (pygame.Surface): Screen to which object will be drawn to.
        image (pygame.Image): Image of game object.
        rect (pygame.Rect): Bounding rectangle of game object.
        pos (Vec2d): Current position of game object.
    """

    def __init__(self, screen, image, pos):
        """
                Initialize drawable game object.
        """
        Sprite.__init__(self)

        # Instance attriutes.
        self.screen = screen
        self.image = image
        self.rect = None  # Is initialized before drawing of init.
        self.pos = pos

    def updateRect(self):
        """
        Update bounding rectangle of game object.
        """
        imageWidth, imageHeight = self.image.get_size()

        # Center bounding rectangle.
        self.rect = self.image.get_rect().move(
            self.pos.x - imageWidth / 2,
            self.pos.y - imageHeight / 2)

    def blitObject(self):
        """
        Draw game object to screen.
        """

        # First update object rectangle.
        self.updateRect()

        # Draw to screen.
        self.screen.blit(self.image, self.rect)
