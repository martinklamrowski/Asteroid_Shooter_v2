import pygame

import colors
import config

from ship.ship import Ship
from utils.vec2d import Vec2d
from bullet.bullet_controller import BulletController


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

    def draw(self):
        """
        Draws all relevant game objects to the screen.
        """
        self.screen.fill(colors.black)

        # Draw ship and bullets from it's bullet controller.
        self.ship.blitMe()
        self.shipBulletController.blitBullets()

        # Actually draw all objects to the screen.
        pygame.display.flip()
