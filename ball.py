'''
ball.py
    This file holds the ball class which is derived from the Sprite class
    The ball class defines the behavior of the ball, such as speed and where to draw on screen
'''
import pygame
import math
import constants

class Ball(pygame.sprite.Sprite):
    """ This class represents the ball
        It derives from the "Sprite" class in Pygame """
 
    # Speed in pixels per cycle
    speed = 10.0
 
    # Floating point representation of where the ball is
    x = 0.0
    y = 180.0
 
    # Direction of ball (in degrees)
    direction = 200
 
    width = 10
    height = 10
 
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create the image of the ball
        self.image = pygame.Surface([self.width, self.height])
 
        # Color the ball
        self.image.fill(constants.white)
 
        # Get a rectangle object that shows where our image is
        self.rect = self.image.get_rect()
 
        # Get attributes for the height/width of the screen
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
 
    def bounce(self, diff):
        """ This function will bounce the ball
            off a horizontal surface (not a vertical one) """
 
        self.direction = (180 - self.direction) % 360
        self.direction -= diff
 
    def update(self):
        """ Update the position of the ball. """
        # Sine and Cosine work in degrees, so we have to convert them
        direction_radians = math.radians(self.direction)
 
        # Change the position (x and y) according to the speed and direction
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)
 
        # Move the image to where our x and y are
        self.rect.x = self.x
        self.rect.y = self.y
 
        # Do we bounce off the top of the screen?
        if self.y <= 0:
            self.bounce(0)
            self.y = 1
 
        # Do we bounce off the left of the screen?
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1
 
        # Do we bounce of the right side of the screen?
        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.width - 1
 
        # Did we fall off the bottom edge of the screen?
        if self.y > 600:
            return True
        else:
            return False