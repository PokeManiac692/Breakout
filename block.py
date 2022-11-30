'''
block.py
    This file holds the Block class for our breakout game.
    Each block is defined using the block class and given information for how to draw it
    such as color, size, and where to draw it on screen
'''

import pygame
import constants

class Block(pygame.sprite.Sprite):
    """This class represents each block that will get knocked out by the ball
    It derives from the "Sprite" class in Pygame """
 
    def __init__(self, color, x, y):
        """ Constructor. Pass in the color of the block,
            and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create the image of the block of appropriate size
        # The width and height are sent as a list for the first parameter.
        self.image = pygame.Surface([constants.block_width, constants.block_height])
 
        # Fill the image with the appropriate color
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
 
        # Move the top left of the rectangle to x,y.
        # This is where our block will appear..
        self.rect.x = x
        self.rect.y = y