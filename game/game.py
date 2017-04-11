import pygame

import colors
import config


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

        pass

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

    def update(self, timePassed):
        """
        Updates all relevant game objects with timePassed.

        Args:
            timePassed: Time between last and current frame.
        """
        pass

    def draw(self):
        """
        Draws all relevant game objects to the screen.
        """
        self.screen.fill(colors.black)

        # Actually draw all objects to the screen.
        pygame.display.flip()