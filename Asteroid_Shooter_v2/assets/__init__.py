"""
Contains all image objects for the game.
"""

import pygame

# Ship assets
shipImageDir = 'Asteroid_Shooter_v2/assets/ship/ship.png'
transparentShipImageDir = 'Asteroid_Shooter_v2/assets/ship/transparentShip.png'

shipImage = pygame.image.load(shipImageDir)
transparentShipImage = pygame.image.load(transparentShipImageDir)

bulletImageDir = 'Asteroid_Shooter_v2/assets/ship/bullet.png'
bulletImage = pygame.image.load(bulletImageDir)

heartImageDir = 'Asteroid_Shooter_v2/assets/ship/heart16.png'
heartImage = pygame.image.load(heartImageDir)

# Asteroid assets
asteroidImageDir = 'Asteroid_Shooter_v2/assets/asteroid/asteroid.png'
asteroidImage = pygame.image.load(asteroidImageDir)

homingAsteroidImageDir = 'Asteroid_Shooter_v2/assets/asteroid/homing_asteroid.png'
homingAsteroidImage = pygame.image.load(homingAsteroidImageDir)

# Powerup assets
bulletSpamImageDir = 'Asteroid_Shooter_v2/assets/powerups/bolt16.png'
bulletSpamImage = pygame.image.load(bulletSpamImageDir)

wideBulletImageDir = 'Asteroid_Shooter_v2/assets/powerups/wide20.png'
wideBulletImage = pygame.image.load(wideBulletImageDir)
"""
deflectorImageDir = 'Asteroid_Shooter_v2/assets/powerups/deflector.png'
deflectorShieldImage = pygame.image.load(delflectorImageDir)
"""
# Music
backgroundSoundDir = 'Asteroid_Shooter_v2/assets/music/background.ogg'
bulletSoundDir = 'Asteroid_Shooter_v2/assets/music/bullet.ogg'
shipHitSoundDir = 'Asteroid_Shooter_v2/assets/music/hit.ogg'

# Ship explosion images
shipExplosionDirPref = 'Asteroid_Shooter_v2/assets/gameover/explosion'
shipExplosionDirs = [shipExplosionDirPref + '%i.png' % i for i in range(1, 11)]
shipExplosionImages = [pygame.image.load(path) for path in shipExplosionDirs]
