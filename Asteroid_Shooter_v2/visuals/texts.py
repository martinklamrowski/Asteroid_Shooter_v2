import pygame

from ..colors import white
from ..config import scoreboardMarginFromScreen, scoreboardHeight
from ..config import levelTextHeight, levelTextMarginFromScreen


class Scoreboard(object):

    def __init__(self, screen, stats):

        self.screen = screen
        self.gameStats = stats
        self.height = scoreboardHeight
        self.marginFromScreen = scoreboardMarginFromScreen
        self.color = white

        self.prefixText = 'Score: '
        self.text = ''

        self.font = pygame.font.Font(pygame.font.get_default_font(),
                                     self.height)

    def updateText(self):
        self.text = self.prefixText + str(self.gameStats['score'])

    def blitMe(self):

        self.updateText()

        curText = self.font.render(self.text, 1, self.color)
        curTextWidth, curTextHeight = curText.get_size()

        screenWidth, _ = self.screen.get_size()

        curTextX = screenWidth - curTextWidth - self.marginFromScreen
        curTextY = self.marginFromScreen

        self.screen.blit(curText, (curTextX, curTextY))


class LevelText(object):

    def __init__(self, screen, stats):

        self.screen = screen
        self.gameStats = stats
        self.height = levelTextHeight
        self.marginFromScreen = levelTextMarginFromScreen
        self.color = white

        self.prefixText = 'Level: '
        self.text = ''

        self.font = pygame.font.Font(pygame.font.get_default_font(),
                                     self.height)

    def updateText(self):
        self.text = self.prefixText + str(self.gameStats['level'])

    def blitMe(self):

        self.updateText()

        curText = self.font.render(self.text, 1, self.color)
        curTextWidth, curTextHeight = curText.get_size()

        screenWidth, _ = self.screen.get_size()

        curTextX = screenWidth - curTextWidth - self.marginFromScreen
        curTextY = scoreboardHeight + scoreboardMarginFromScreen

        self.screen.blit(curText, (curTextX, curTextY))
