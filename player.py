'''
player.py
    The player file holds the Player class, which defines our player bar in breakout.
    As the user moves the mouse, the player class manages the intended behaviors of the player
    bar at the bottom of the screen
'''

import pygame
import constants

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls. """
 
    def __init__(self):
        """ Constructor for Player. """
        # Call the parent's constructor
        super().__init__()
 
        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((constants.white))
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
 
        self.rect.x = 0
        self.rect.y = self.screenheight-self.height
 
    def update(self):
        """ Update the player position. """
        # Get where the mouse is
        pos = pygame.mouse.get_pos()
        # Set the left side of the player bar to the mouse position
        self.rect.x = pos[0]
        # Make sure we don't push the player paddle
        # off the right side of the screen
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width