import pygame

from utils import *
from sprite import MySprite


def create_text(text: str):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    return myfont.render(text, False, (100, 100, 0))

class Story():

    def __init__(self, screen):
        self.screen = screen
        # Load all background images
        self.bg_dragon_castle = MySprite('pictures/dragon_castle.jpg')
        self.bg_lock_sword = MySprite('pictures/sword_lockpick.jpg')
        self.bg_goblin = MySprite('pictures/goblin.jpg')
        #self.bg_tower_dungeon = MySprite('pictures/tower_dungeon.jpg') #
        #self.bg_princess_door = MySprite('pictures/princess_door.jpg') #
        self.bg_princess_room = MySprite('pictures/dragon_fight.jpg')
        self.bg_castle_princess = MySprite('pictures/castle_princess.jpg')
        self.bg_victory_castle = MySprite('pictures/lonely_castle.jpg')
        self.bg_victory_princess = MySprite('pictures/lonely_princess.jpg')
        self.lockpick = False
        self.sword = False
        self.pinky = True
        self.tower = False
        self.dungeon = False
        self.fight = False
        self.sneak = False
        self.story_generator = self._story_generator()
        self.story_loop('')
        self.valid_text = False

    def story_loop(self, txt):
        """
        Wrapper for story generator
        :param txt:
        :return: True if story continues. False when finished
        """
        self.input_text = txt.lower()
        self.valid_text = False
        try:
            next(self.story_generator)
        except StopIteration:
            return False
        return True


    def _story_generator(self):
        """
        Story loop of game, a generator that requires valid text to continue
        :param txt: Input text passed in from main loop
        """

        # Quest stage
        self.bg_dragon_castle.draw(self.screen)

        txt = 'A princess has been captured by a dragon. The king has offered a castle as a reward for rescuing her.\n' +\
                         'Choose your equipment for the adventure (lockpick or sword)'
        render_text_centered(txt, self.screen, TEXT_X, TEXT_Y, S_WIDTH)
        valid_text = False
        while not valid_text:
            if not self.input_text:
                yield
            elif self.input_text[0] == 'l':
                self.lockpick = True
                valid_text = True
            elif self.input_text[0] == 's':
                self.sword = True
                valid_text = True
            else:
                #print('You must enter "lockpick" or "sword"')
                yield

        self.valid_text = True
        self.input_text = ''
        self.screen.fill((0,0,0))

        # Quest stage
        self.bg_lock_sword.draw(self.screen)

        valid_text = False
        while not valid_text:
            txt = "You approach the dragon's castle, a goblin guards the entrance.\n" + \
                            "Do you fight the goblin or sneak past? (fight or sneak): "
            render_text_centered(txt, self.screen, TEXT_X, TEXT_Y, S_WIDTH)
            valid_text = False
            while not valid_text:
                if not self.input_text:
                    yield
                elif self.input_text[0] == 'f':
                    self.fight = True
                    valid_text = True
                elif self.input_text[0] == 's':
                    self.sneak = True
                    valid_text = True
                else:
                    #print('You must enter "fight" or "sneak"')
                    yield

        if self.fight:
            if self.sword:
                print('You defeat the goblin with your sword')
            else:
                print('You have no sword! While fighting, the goblin manages to nibble your pinky off')
                pinky = False

        if self.sneak:
            if self.sword:
                print(
                    'The goblin catches a glimpse of your big shiny sword! While fighting, the goblin manages to nibble your pinky off')
                pinky = False
            else:
                print('You manage to sneak past the goblin')
