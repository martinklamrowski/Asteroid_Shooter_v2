from asteroid import Asteroid
from homing_asteroid import HomingAsteroid


class AsteroidController(object):
    """
    Class that controlls spawning, updating, and maintaining of asteroids.

    Attributes:
        screen (pygame.Surface): Screen to which asteroids will be drawn to.
        ship (Ship): Ship which homing asteroid will follow around.
        asteroids (list of Asteroid): Child asteroids of controller.
    """
    def __init__(self, screen, ship):

        # Asteroid controller attributes.
        self.screen = screen
        self.ship = ship
        self.asteroids = []

    def spawnBasicAsteroid(self):
        self.asteroids.append(Asteroid(self.screen))

    def spawnHomingAsteroid(self):
        self.asteroids.append(HomingAsteroid(self.screen, self.ship))

    def maintainAsteroids(self):
        for asteroid in self.asteroids:
            if not asteroid.isActive():
                self.asteroids.remove(asteroid)

    def updateAsteroids(self, timePassed):
        for asteroid in self.asteroids:
            asteroid.update(timePassed)

    def blitAsteroids(self):
        for asteroid in self.asteroids:
            asteroid.blitMe()
