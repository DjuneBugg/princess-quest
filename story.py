import pygame

from utils import *
from sprite import MySprite


def create_text(self, text: str):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    return myfont.render(text, False, (100, 100, 0))

class Story():

    def __init__(self, screen):
        # Load all background images
        self.bg_dragon_castle = MySprite('pictures/dragon_castle.jpg')
        self.bg_lock_sword = MySprite('pictures/sword_lockpick.jpg')
        self.bg_goblin = MySprite('pictures/goblin.jpg')
        self.bg_tower_dungeon = MySprite('pictures/tower_dungeon.jpg') #
        self.bg_princess_door = MySprite('pictures/princess_door.jpg') #
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

    def story_loop(self, txt):
        """
        Story loop of game, a generator that requires valid text to continue
        :param txt: Input text passed in from main loop
        """
        self.bg_dragon_castle.draw()
        ts = create_text('A princess has been captured by a dragon. The king has offered a castle as a reward for rescuing her.\n'
                         'Choose your equipment for the adventure (lockpick or sword): ')
        self.screen.blit(ts, (TEXT_X, TEXT_Y))

        valid_text = False
        while not valid_text:
            if txt.lower() == 'lockpick':
                self.lockpick = True
                valid_text = True
            elif txt.lower() == 'sword':
                self.sword = True
                valid_text = True
            else:
                print('You must enter "lockpick" or "sword"')
                yield

