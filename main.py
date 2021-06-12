from typing import *
import pygame
import sys

from utils import *
from sprite import MySprite
from story import Story

# define a main function
def main():
    # initialize the pygame module
    pygame.init()

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    # Initialise text
    pygame.font.init()  # you have to call this at the start,

    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Welcome to Princess Quest!', False, (100, 100, 0))

    background = MySprite('pictures/dragon_castle.jpg')
    background.draw(screen)
    #screen.blit(background.image, background.rect)
    screen.blit(textsurface, (TEXT_X, TEXT_Y))
    pygame.display.flip()
    my_group = pygame.sprite.Group(background)
    # Text handling
    user_text = ''
    input_rect = pygame.Rect(INPUT_X, INPUT_Y, 140, 50)

    # main loop
    while True:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Did the user hit a key?
            elif event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                # Unicode standard is used for string formation
                else:
                    user_text += event.unicode

        #my_group.update()
        #my_group.draw(screen)
        #screen.blit(background.image, background.rect)

        # Draw input text box
        #pygame.draw.rect(screen, pygame.Color('DarkGoldenrod'), input_rect)
        pygame.draw.rect(screen, (100,100,0), input_rect)
        # Draw input text
        text_surface = myfont.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        # set width of textfield so that text cannot get outside of user's text input
        input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.display.flip()



# Main entry point for script
if __name__ == '__main__':
    main()