import random


class EventSpawner(object):

    def __init__(self, asteroidController, powerupController):

        self.asteroidController = asteroidController
        self.powerupController = powerupController

        self.events = {self.asteroidController.spawnBasicAsteroid: 100,
                       self.asteroidController.spawnHomingAsteroid: 20,
                       self.powerupController.spawnRandomPowerup: 1,
                       self.noEvent: 2000}

    def spawnRandomEvent(self):
        event = self.getRandomEvent()
        event()

    def getRandomEvent(self):
        totalChances = sum(self.events.values())

        randomChance = random.randint(1, totalChances)

        for event, eventChance in self.events.items():
            if randomChance <= eventChance:
                return event
            else:
                randomChance -= eventChance

        raise Exception('Not suppossed to reach here.')

    def noEvent(self):
        pass
