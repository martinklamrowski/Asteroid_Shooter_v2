import pygame


def doCollide(a, b):
    if simpleCollision(a, b):
        return complexCollision(a, b)
    return 0


def simpleCollision(spriteOne, spriteTwo):
    """
    Simple bounding box collision detection.
    """
    widthSpriteOne, heightSpriteOne = spriteOne.image.get_size()

    rectSpriteOne = spriteOne.image.get_rect().move(
        spriteOne.pos.x - widthSpriteOne / 2,
        spriteOne.pos.y - heightSpriteOne / 2)

    widthSpriteTwo, heightSpriteTwo = spriteTwo.image.get_size()

    rectSpriteTwo = spriteTwo.image.get_rect().move(
        spriteTwo.pos.x - widthSpriteTwo / 2,
        spriteTwo.pos.y - heightSpriteTwo / 2)

    return rectSpriteOne.colliderect(rectSpriteTwo)


def complexCollision(spriteOne, spriteTwo):
    """
    Collision detection through image masks.
    """
    return pygame.sprite.collide_mask(spriteOne, spriteTwo) is not None
