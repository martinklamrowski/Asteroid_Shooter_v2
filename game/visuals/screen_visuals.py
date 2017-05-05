from bullet_guage import BulletGuage


class VisualsController(object):
    """
    Controller class that holds, updates, and draws all on screen visual
    elements.

    List of the screen visuals:
        1. Bullet Guage
        2. Health Bar
        3. Score/Level

    Attributes:
        screen (pygame.Surface): Screen to which visuals will be drawn to.
        asteroidController (AsteroidController): Controller of game asteroids.
        bulletController (BulletController): Controller of ship bullets.
        ship (Ship): Player's ship.
        visuals (list): List of visual elements the controller owns.
    """

    def __init__(self, screen, asteroidController, bulletController, ship):

        self.screen = screen

        self.asteroidController = asteroidController
        self.bulletController = bulletController
        self.ship = ship

        self.visuals = []

        # Add bullet guage visual.
        self.visuals.append(BulletGuage(self.screen, self.bulletController))

    def blitMe(self):
        for visual in self.visuals:
            visual.blitMe()
