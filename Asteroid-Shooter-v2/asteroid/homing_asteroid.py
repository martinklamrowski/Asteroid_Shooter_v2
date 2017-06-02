from .asteroid import Asteroid
from ..assets import homingAsteroidImage
from ..config import homingAsteroidTranslationSpeed
from ..config import homingAsteroidRotationSpeed


class HomingAsteroid(Asteroid):
    """
    Homing asteroid is an asteroid that follows the player's ship around.

    Attributes:
        screen (pygame.Surface): Screen to which the asteroid is drawn to.
        image (pygame.Image): Image of the asteroid.
        rect (pygame.Rect): Bounding box of the asteroid.
        pos (Vec2d): Position of the asteroid.
        direction (Vec2d): Directigon of the asteroid.
        asteroidTranslationSpeed (float): Asteroid speed translationally.
        asteroidRotationSpeed (float): Asteroid speed rotationally.
        ship (Ship): Instance of the ship the homing asteroid is following.
    """

    def __init__(self, screen, ship):

        super(HomingAsteroid, self).__init__(screen)

        self.image = homingAsteroidImage
        self.asteroidTranslationSpeed = homingAsteroidTranslationSpeed
        self.asteroidRotationSpeed = homingAsteroidRotationSpeed

        self.ship = ship

    def update(self, timePassed):
        """
        Three components to the homing asteroid update:
          1. Update time the homing asteroid has been alive.
          2. Update the position of the homing asteroid with the current
          direction.
          3. Change direction of the homing asteroid towards the ship.
        """

        self.timeAlive += timePassed

        self.pos += self.direction * timePassed * self.asteroidTranslationSpeed

        self.updateAsteroidAngle()

    def updateAsteroidAngle(self):
        angleWanted = (self.ship.pos - self.pos).get_angle()
        currentAsteroidAngle = self.direction.get_angle()

        angleDifference = angleWanted - currentAsteroidAngle

        # Normalize angle difference to be between -180 and 180 degrees.

        if angleDifference > 180.0:
            angleDifference -= 360.0

        if angleDifference < -180.0:
            angleDifference += 360.0

        # If the angle difference is positive, that means it is best to rotate
        # in that direction to get to the ship the fastest. And vice versa if
        # the angle difference is negative.

        if angleDifference > 0.0:
            self.direction.rotate(self.asteroidRotationSpeed)
        else:
            self.direction.rotate(-self.asteroidRotationSpeed)
