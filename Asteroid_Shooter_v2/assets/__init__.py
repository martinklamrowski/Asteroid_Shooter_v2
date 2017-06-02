"""
Contains all image objects for the game.
"""

import pygame

# Ship assets
shipImageDir = 'game/assets/ship/ship.png'
transparentShipImageDir = 'game/assets/ship/transparentShip.png'

shipImage = pygame.image.load(shipImageDir)
transparentShipImage = pygame.image.load(transparentShipImageDir)

bulletImageDir = 'game/assets/ship/bullet.png'
bulletImage = pygame.image.load(bulletImageDir)

heartImageDir = 'game/assets/ship/heart16.png'
heartImage = pygame.image.load(heartImageDir)

# Asteroid assets
asteroidImageDir = 'game/assets/asteroid/asteroid.png'
asteroidImage = pygame.image.load(asteroidImageDir)

homingAsteroidImageDir = 'game/assets/asteroid/homing_asteroid.png'
homingAsteroidImage = pygame.image.load(homingAsteroidImageDir)

# Powerup assets
bulletSpamImageDir = 'game/assets/powerups/bolt16.png'
bulletSpamImage = pygame.image.load(bulletSpamImageDir)

wideBulletImageDir = 'game/assets/powerups/wide20.png'
wideBulletImage = pygame.image.load(wideBulletImageDir)

# Music
backgroundSoundDir = 'game/assets/music/background.ogg'
bulletSoundDir = 'game/assets/music/bullet.ogg'
shipHitSoundDir = 'game/assets/music/hit.ogg'

# Ship explosion images
shipExplosionDirPref = 'game/assets/gameover/explosion'
shipExplosionDirs = [shipExplosionDirPref + '%i.png' % i for i in range(1, 11)]
shipExplosionImages = [pygame.image.load(path) for path in shipExplosionDirs]
