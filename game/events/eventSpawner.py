import random


class EventSpawner(object):

    def __init__(self, asteroidController):

        self.asteroidController = asteroidController

        self.events = {self.spawnBasicAsteroid: 100,
                       self.noEvent: 1000}

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

    def spawnBasicAsteroid(self):
        self.asteroidController.spawnBasicAsteroid()

    def noEvent(self):
        pass
