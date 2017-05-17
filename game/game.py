import pygame

import colors
import config

from asteroid.asteroid_controller import AsteroidController
from events.eventSpawner import EventSpawner

from ship.ship import Ship
from utils.vec2d import Vec2d
from utils.collisions import doCollide
from bullet.bullet_controller import BulletController
from visuals.screen_visuals import VisualsController
from powerups.powerup_controller import PowerupController


class Game(object):

    def __init__(self):

        # Initialize imported pygame modules.
        pygame.init()

        # Initialize screen object.
        # All visual game objects will have a refrence to this
        # screen object so they can draw to it.
        self.screen = pygame.display.set_mode(
            (config.screenWidth, config.screenHeight),
            0, 32)

        # Clock is used to track and control the framerate of the game.
        self.clock = pygame.time.Clock()

        # Game states
        self.paused = 0
        self.running = 1

        # Game objects
        initialShipPos = Vec2d((config.screenWidth / 2,
                                config.screenHeight / 2))
        self.ship = Ship(self.screen, initialShipPos)
        self.shipBulletController = BulletController(self.screen,
                                                     self.ship)

        self.asteroidController = AsteroidController(self.screen, self.ship)

        # Powerup controller
        self.powerupController = PowerupController(self.screen, self.ship,
                                                   self.shipBulletController)

        # Event spawner
        self.eventSpawner = EventSpawner(self.asteroidController,
                                         self.powerupController)

        # Screen visuals
        self.visualsController = VisualsController(self.screen,
                                                   self.asteroidController,
                                                   self.shipBulletController,
                                                   self.ship)

    def run(self):

        while self.running:

            # Get time between last and current frame.
            timePassed = self.clock.tick(config.framerate)

            self.handleKeyboardEvents()

            if not self.paused:
                self.update(timePassed)

            self.draw()

    def handleKeyboardEvents(self):
        """
        Get all keyboard events and handles them accordingly.

        Keyboard events related to game states(paused, running,...)
        should only be handled when the key is pressed down(not held).

        Keyboard events related to game actions are handled whenever.
        """

        # Handle keyboard events for game states.
        for event in pygame.event.get():

            # Handle if user closed pygame window.
            if event.type == pygame.QUIT:
                self.running = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = 0
                elif event.key == pygame.K_p:
                    self.paused = not self.paused

        keysPressed = pygame.key.get_pressed()
        # Send keyboard input to ship
        self.ship.getKeyboardInput(keysPressed)
        self.shipBulletController.getKeyboardInput(keysPressed)

    def update(self, timePassed):
        """
        Updates all relevant game objects with timePassed.

        Args:
            timePassed: Time between last and current frame.
        """

        # Update ship and it's bullet controller.
        self.ship.update(timePassed)
        self.shipBulletController.update(timePassed)

        # Update asteroids, through their controller.
        self.asteroidController.updateAsteroids(timePassed)

        # Update powerups.
        self.powerupController.updatePowerups(timePassed)

        # Handle collisions.
        self.handleCollisions()

        # Spawn new events
        self.eventSpawner.spawnRandomEvent()

        # Maintain game objects.
        self.maintainGameObjects()

    def draw(self):
        """
        Draws all relevant game objects to the screen.
        """
        self.screen.fill(colors.black)

        # Draw ship and bullets from it's bullet controller.
        self.ship.blitMe()
        self.shipBulletController.blitBullets()

        # Draw asteroids.
        self.asteroidController.blitAsteroids()

        # Draw powerups.
        self.powerupController.drawPowerups()

        # Draw screen visuals.
        self.visualsController.blitMe()

        # Actually draw all objects to the screen.
        pygame.display.flip()

    def maintainGameObjects(self):
        # Maintain bullets.
        self.shipBulletController.maintainBullets()

        # Maintain asteroids.
        self.asteroidController.maintainAsteroids()

        # Maintain powerups.
        self.powerupController.maintainPowerups()

    def handleCollisions(self):

        # Between ship and asteroids.
        if not self.ship.isInvincible:
            for asteroid in self.asteroidController.asteroids:
                if doCollide(self.ship, asteroid):
                    # Remove asteroid.
                    self.asteroidController.asteroids.remove(asteroid)

                    # Tell ship it has collided with an asteroid.
                    isShipAlive = self.ship.shipCollided()

                    if not isShipAlive:
                        self.initializeGameOverSequence()
                        return

        # Between bullet and asteroids.
        for bullet in self.shipBulletController.bullets:
            for asteroid in self.asteroidController.asteroids:
                if doCollide(bullet, asteroid):
                    # Remove bullet and asteroid, and move on to next bullet.
                    self.shipBulletController.bullets.remove(bullet)
                    self.asteroidController.asteroids.remove(asteroid)

                    break

        # Between ship and powerups.
        self.powerupController.handleCollisionsWithShip()

    def initializeGameOverSequence(self):
        self.running = 0
