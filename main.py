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
    #screen = pygame.display.set_mode((S_WIDTH+200, S_HEIGHT+200))
    screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    change_screen_size(screen.get_width(), screen.get_height())

    # Initialise text
    pygame.font.init()  # you have to call this at the start,

    # Text handling
    user_text = ''
    input_font = pygame.font.SysFont('Comic Sans MS', 30)
    input_rect = pygame.Rect(INPUT_X, INPUT_Y, 140, 50)
    input_rect_colour = (0,0,0)

    # Create story
    story = Story(screen)

    # main loop
    more_story = True
    while more_story:
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
                elif event.key == pygame.K_RETURN:
                    more_story = story.story_loop(user_text)
                    if story.valid_text:
                        user_text = ''
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # Unicode standard is used for string formation
                else:
                    user_text += event.unicode

        # Draw input text box
        pygame.draw.rect(screen, input_rect_colour, input_rect)
        # Draw input text
        text_surface = input_font.render(user_text, True, (100, 100, 0))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        # set width of textfield so that text cannot get outside of user's text input
        input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Main entry point for script
if __name__ == '__main__':
    main()