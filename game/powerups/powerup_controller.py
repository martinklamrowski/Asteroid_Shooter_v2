
class PowerupController(object):
    """
    Class that controlls spawning, updating, and drawing of powerups.

    Attributes:
        screen (pygame.Surface): Screen to which asteroids will be drawn to.
        powerups (list of Powerups): Child powerups of controller.
    """

    def __init__(self, screen):

        self.screen = screen
        self.powerups = []

    def updatePowerups(self, timePassed):
        for powerup in self.powerups:
            powerup.update(timePassed)

    def drawPowerups(self):
        for powerup in self.powerups:
            powerup.blitMe()
