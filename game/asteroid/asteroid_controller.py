from asteroid import Asteroid


class AsteroidController(object):
    """
    Class that controlls spawning, updating, and maintaining of asteroids.

    Attributes:
        screen (pygame.Surface): Screen to which asteroids will be drawn to.
        asteroids (list of Asteroid): Child asteroids of controller.
    """
    def __init__(self, screen):

        # Asteroid controller attributes.
        self.screen = screen
        self.asteroids = []

    def spawnBasicAsteroid(self):
        self.asteroids.append(Asteroid(self.screen))

    def maintainAsteroids(self):
        raise NotImplementedError

    def updateAsteroids(self, timePassed):
        for asteroid in self.asteroids:
            asteroid.update(timePassed)

    def blitAsteroids(self):
        for asteroid in self.asteroids:
            asteroid.blitMe()
