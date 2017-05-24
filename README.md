# Asteroid Shooter v2.0
The new and improved version to my first video game. 

A few years back I wrote the first version of this asteroid shooter game, and in the meantime I have learned a lot about design patterns and general good practices. So I decided to put these new skills to the test by recreating my rookie project.

IMPROVEMENTS
------------
1. Decoupling of game objects from the main game class.
    * **In version 1.0:** All game object instances and the logic between them was stored in the main game class. This made what the actual game class was doing unclear, instead of simply being a deligator of the game logic.

    * **New and improved:** Groups of similiar game objects (i.e. asteroids or powerups) are abstracted under a 'controller' object. These controllers store the objects, maintain them, and delegate updates and when to be drawn to screen.

    * **How does that affect me...the programmer?:** Adding new features/game objects is so simple. Just code up the new game object in isolation, abstract under a controller and add a few calls to that new controller object in the main game code. And lets not even get into how much easier testing is.

REQUIREMENTS
------------
* Python 2.x
* Pygame

You can install all requirements through pip with:
`pip install -r requirements.txt`

CONFIGURATION
-------------

Just run `python main.py`. 

CONTROLS
--------
I - Up

K - Down

J - Left

L - Right

A - Rotate left

D - Rotate right

SPACE - Shoot

P - Pause

