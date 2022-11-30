'''
Creating a Breakout Game Using Pygame
- This example creates a game using multiple files.
  These abstractions allow developers to work on individual parts of a program separately
  while building towards a larger program!
'''

import pygame

# connect game objects from other files used
import ball
import block
import constants
import player

# initializing the constructor
pygame.init()

# opens up a window w/game title
screen = pygame.display.set_mode(constants.resolution)

# set window caption
pygame.display.set_caption('Breakout')

# Load title image file
titleImg = pygame.image.load('BreakoutTitle.png')


# Title Function (x, y coordinates to plot)
def title(x, y):
    screen.blit(titleImg, (x, y))


# get and store screen width in a variable
width = screen.get_width()

# get and store screen height in a variable
height = screen.get_height()

# defining fonts
font = pygame.font.Font(None, 50)
smallfont = pygame.font.SysFont('Roboto', 35)

# render text using above font
text = smallfont.render('Quit', True, constants.white)
startText = smallfont.render('Start Game', True, constants.white)

# Menu Loop
while True:
    # stores mouse (x,y) coordinates into the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # set up event listeners
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # checks if mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if clicked within button parameters:
            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 60 <= mouse[1] <= height / 2 - 20:
                # make the mouse disappear when over our window
                pygame.mouse.set_visible(0)

                # Create a surface we can draw on
                background = pygame.Surface(screen.get_size())

                # Create sprite lists
                blocks = pygame.sprite.Group()
                balls = pygame.sprite.Group()
                allsprites = pygame.sprite.Group()

                # Create the player paddle object
                player = player.Player()
                allsprites.add(player)

                # Create the ball
                ball = ball.Ball()
                allsprites.add(ball)
                balls.add(ball)

                # The top of the block (y position)
                top = 80

                # Number of blocks to create
                blockcount = 32

                # --- Create blocks

                # Five rows of blocks
                for row in range(5):
                    # 32 columns of blocks
                    for column in range(0, blockcount):
                        # Create a block (color,x,y)
                        block1 = block.Block(constants.blue, column * (constants.block_width + 2) + 1, top)
                        # add blocks to our lists
                        blocks.add(block1)
                        allsprites.add(block1)
                    # Move the top of the next row down
                    top += constants.block_height + 2

                # Clock to limit speed
                clock = pygame.time.Clock()

                # Is the game over?
                game_over = False

                # Exit the program?
                exit_program = False

                # Main program loop
                while not exit_program:

                    # Limit to 30 fps
                    clock.tick(30)

                    # Clear the screen
                    screen.fill(constants.black)

                    # Process events in the game
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit_program = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                exit_program = True

                    # Update the ball and player position as long
                    # as the game is not over.
                    if not game_over:
                        # Update the player and ball positions
                        player.update()
                        game_over = ball.update()

                    # See if the ball hits the player paddle
                    if pygame.sprite.spritecollide(player, balls, False):
                        # The 'diff' lets you try to bounce the ball left or right
                        # depending where on the paddle you hit it
                        diff = (player.rect.x + player.width / 2) - (ball.rect.x + ball.width / 2)

                        # Set the ball's y position in case
                        # we hit the ball on the edge of the paddle
                        ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
                        ball.bounce(diff)

                    # If we are done, print game over
                    if game_over:
                        text = font.render("Game Over", True, constants.white)
                        textpos = text.get_rect(centerx=background.get_width() / 2)
                        textpos.top = 300
                        screen.blit(text, textpos)

                    # Check for collisions between the ball and the blocks
                    deadblocks = pygame.sprite.spritecollide(ball, blocks, True)

                    # If we hit a block, bounce the ball
                    if len(deadblocks) > 0:
                        ball.bounce(0)

                        # Game ends if all the blocks are gone
                        if len(blocks) == 0:
                            game_over = True

                    # Draw Everything
                    allsprites.draw(screen)

                    # Flip the screen and show what we've drawn
                    pygame.display.flip()
            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()

    # fills the screen with a color
    screen.fill((0, 0, 0))

    # if mouse is hovered on a button it changes to lighter shade
    # Start Button
    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 60 <= mouse[1] <= height / 2 - 20:
        pygame.draw.rect(screen, constants.color_light, [width / 2 - 70, height / 2 - 60, 140, 40])
    else:
        pygame.draw.rect(screen, constants.color_dark, [width / 2 - 70, height / 2 - 60, 140, 40])

    # Quit Button
    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 <= mouse[1] <= height / 2 + 40:
        # (Where to draw, color, top left corner coordinate, size of rectangle)
        pygame.draw.rect(screen, constants.color_light, [width / 2 - 70, height / 2, 140, 40])
    else:
        pygame.draw.rect(screen, constants.color_dark, [width / 2 - 70, height / 2, 140, 40])

    # Blit title image
    title(width / 4, height / 4 - 60)
    # superimposing the Start Text on start button
    screen.blit(startText, (width / 2 - 65, height / 2 - 50))
    # superimposing the text onto our quit button
    screen.blit(text, (width / 2 - 25, height / 2 + 5))

    # updates the frames of the game
    pygame.display.update()
