# import the pygame module, so you can use it
import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

# define a main function
def main():
    # initialize the pygame module
    pygame.init()

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((680, 480))

    # Initialise text
    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Welcome to Princess Quest!', False, (0, 0, 0))

    # define a variable to control the main loop
    running = True

    background1 = Background('pictures/dragon_castle.jpg', [0, 0])
    background2 = Background('pictures/goblin.jpg', [0, 0])
    background = background1
    screen.blit(background.image, background.rect)
    screen.blit(textsurface, (0, 0))
    pygame.display.flip()


    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # Did the user hit a key?
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if background == background1:
                        background = background2
                    else:
                        background = background1
                # Add text
                screen.fill((0, 0, 0))
                screen.blit(background.image, background.rect)
                screen.blit(textsurface, (0, 0))
                pygame.display.flip()

# Main entry point for script
if __name__ == '__main__':
    main()