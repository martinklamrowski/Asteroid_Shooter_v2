from bullet_guage import BulletGuage
from health_bar import HealthBar
from texts import Scoreboard, LevelText


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

    def __init__(self, screen, asteroidController,
                 bulletController, ship, stats):

        self.screen = screen

        self.asteroidController = asteroidController
        self.bulletController = bulletController
        self.ship = ship
        self.gameStats = stats

        self.visuals = []

        # Add bullet guage visual.
        self.visuals.append(BulletGuage(self.screen, self.bulletController))

        # Add health bar visual.
        self.visuals.append(HealthBar(self.screen, self.ship))

        # Add scoreboard.
        self.visuals.append(Scoreboard(self.screen, self.gameStats))

        # Add level text.
        self.visuals.append(LevelText(self.screen, self.gameStats))

    def blitMe(self):
        for visual in self.visuals:
            visual.blitMe()
