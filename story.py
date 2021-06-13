import math
import pygame

from utils import *
from sprite import MySprite


class Story():

    def __init__(self, screen):
        self.screen = screen
        # Load all background images
        self.bg_dragon_castle = MySprite('pictures/dragon_castle.jpg')
        self.bg_lock_sword = MySprite('pictures/sword_lockpick.jpg')
        self.bg_goblin = MySprite('pictures/goblin.jpg')
        self.bg_tower = MySprite('pictures/tower.jpg', scale_box=(0,0,math.floor(B_WIDTH/2), B_HEIGHT))
        self.bg_dungeon = MySprite('pictures/dungeon.jpg', scale_box=(math.floor(B_WIDTH/2),0,math.floor(B_WIDTH/2), B_HEIGHT))
        #self.bg_tower_dungeon = MySprite('pictures/tower_dungeon.jpg') #
        self.bg_princess_door = MySprite('pictures/princess_door.jpg') #
        self.bg_princess_room = MySprite('pictures/dragon_fight.jpg')
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
        self.castle = False
        self.princess = False
        self.story_generator = self._story_generator()
        self.story_loop('')
        self.valid_text = False
        # Rectangle to cover up text for each story
        self.text_rect = pygame.Rect(0, TEXT_Y, S_WIDTH, 300)

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

        # Music
        pygame.mixer.music.load('audio/Magistar.mp3')
        pygame.mixer.music.play(-1)

        ##############################################################
        # Quest stage
        ##############################################################
        self.bg_dragon_castle.draw(self.screen)

        txt = 'A princess has been captured by a dragon. The king has offered a castle as a reward for rescuing her.\n' +\
                         'This is a typing game, type with keyboard and hit enter to continue'
        render_text_centered(txt, self.screen, TEXT_X, TEXT_Y, S_WIDTH)
        yield

        ##############################################################
        # Equipment stage
        ##############################################################
        self.valid_text = True
        self.input_text = ''
        self.screen.fill((0,0,0))
        self.bg_lock_sword.draw(self.screen)

        txt = 'Choose your equipment for the adventure (lockpick[l] or sword[s])'
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

        ##############################################################
        # Goblin stage
        ##############################################################
        self.valid_text = True
        self.input_text = ''
        self.screen.fill((0,0,0))
        self.bg_goblin.draw(self.screen)

        pygame.mixer.music.load('audio/Darkling.mp3')
        pygame.mixer.music.play(-1)

        txt = "You approach the dragon's castle, a goblin guards the entrance.\n" + \
                        "Do you fight the goblin or sneak past? (fight[f] or sneak[s]): "
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
        self.valid_text = True

        # Clear text
        pygame.draw.rect(self.screen, (0,0,0), self.text_rect)
        if self.fight:
            if self.sword:
                txt = 'You defeat the goblin with your sword'
            else:
                txt = 'You have no sword! While fighting, the goblin manages to nibble your pinky off'
                self.pinky = False
        if self.sneak:
            if self.sword:
                txt = 'The goblin catches a glimpse of your big shiny sword! While fighting, the goblin manages to nibble your pinky off'
                self.pinky = False
            else:
                txt = 'You manage to sneak past the goblin'
        render_text_centered(txt, self.screen, TEXT_X, TEXT_Y, S_WIDTH)
        yield

        ##############################################################
        # Tower Dungeon stage
        ##############################################################
        self.valid_text = True
        self.input_text = ''
        self.screen.fill((0,0,0))
        self.bg_tower.draw(self.screen)
        self.bg_dungeon.draw(self.screen)

        txt = 'You enter the castle, do you think the princess is in the tower or the dungeon? (tower[t] or dungeon[d]):'
        render_text_centered(txt, self.screen, TEXT_X, TEXT_Y, S_WIDTH)
        valid_text = False
        while not valid_text:
            if not self.input_text:
                yield
            elif self.input_text[0] == 't':
                self.tower = True
                valid_text = True
            elif self.input_text[0] == 'd':
                self.dungeon = True
                valid_text = True
            else:
                yield

        ##############################################################
        # Princess door stage
        ##############################################################
        self.valid_text = True
        self.input_text = ''
        self.screen.fill((0,0,0))
        self.bg_princess_door.draw(self.screen)

        txt = 'Hooray! You found the princess door, but there is a code'
        give_up = False
        if self.lockpick:
            txt = txt + '\nThankfully you got through the door with the lockpick!'
            render_text_centered(txt, self.screen, TEXT_X, TEXT_Y, S_WIDTH)
            yield
        else:
            txt = txt + '\n6 x Pineapple = 24\nPineapple x Apple = 32\nWhat does apple = ?'
            render_text_centered(txt, self.screen, TEXT_X, TEXT_Y, S_WIDTH)
            valid_text = False
            tries = 0
            while not valid_text:
                if not self.input_text:
                    yield
                elif self.input_text == '8' or self.input_text == 'eight':
                    valid_text = True
                else:
                    if tries < 3:
                        render_text_centered(txt + '\nIncorrect! Try again', self.screen, TEXT_X, TEXT_Y, S_WIDTH)
                        yield
                    elif tries < 10:
                        # Clear text
                        pygame.draw.rect(self.screen, (0, 0, 0), self.text_rect)
                        render_text_centered(txt + '\nIncorrect! Try again (Hint: Pineapple = 4)', self.screen, TEXT_X, TEXT_Y, S_WIDTH)
                        yield
                    else:
                        # Let them through after 10 tries
                        print('You give up and break the door with your sword. Your sword breaks')
                        valid_text = True
                        give_up = True
                    tries = tries + 1

        # Clear text
        pygame.draw.rect(self.screen, (0, 0, 0), self.text_rect)
        if give_up:
            txt = 'You give up and break the door with your sword. Your sword breaks'
            self.sword = False
        else:
            txt = ''
        self.valid_text = True
        self.input_text = ''
        self.screen.fill((0,0,0))
        self.bg_princess_room.draw(self.screen)

        pygame.mixer.music.load('audio/BurntSpirit.mp3')
        pygame.mixer.music.play(-1)

        txt = txt + "\nYou enter the room and it turns out that the dragon is guarding the princess himself!"
        if self.sword:
            txt = txt + '\nThe dragon breathes fire and melts your sword!'
            self.sword = False
        render_text_centered(txt, self.screen, TEXT_X, TEXT_Y, S_WIDTH)
        yield


        ##############################################################
        # Princess Room stage
        ##############################################################

        # Clear text
        pygame.draw.rect(self.screen, (0, 0, 0), self.text_rect)
        txt = 'The dragon whips his tail at you. The tail is 5 meters long and you are 3 meters away.\n' + \
                        'How far back do you walk (in meters)?'
        render_text_centered(txt, self.screen, TEXT_X, TEXT_Y, S_WIDTH)
        valid_text = False
        while not valid_text:
            if not self.input_text:
                yield
            try:
                number = float(self.input_text)
                if number > 3:
                    # Clear text
                    pygame.draw.rect(self.screen, (0, 0, 0), self.text_rect)
                    render_text_centered(txt + '\nYou stepped too far back and fell onto the stairs. Try again', self.screen, TEXT_X,
                                         TEXT_Y, S_WIDTH)
                    yield
                elif number > 2:
                    txt = 'You dodged it, great job!'
                    valid_text = True
                elif number == 2:
                    # Clear text
                    txt = 'Wow, that was close, but you dodged it, great job!'
                    valid_text = True
                else:
                    # Clear text
                    pygame.draw.rect(self.screen, (0, 0, 0), self.text_rect)
                    render_text_centered(txt + '\nOh no! You got smacked to the ground!', self.screen, TEXT_X,
                                         TEXT_Y, S_WIDTH)
                    yield
            except:
                # Clear text
                pygame.draw.rect(self.screen, (0, 0, 0), self.text_rect)
                render_text_centered(txt + '\nIs that even a number??', self.screen, TEXT_X,
                                     TEXT_Y, S_WIDTH)
                yield

        # Clear text
        pygame.draw.rect(self.screen, (0, 0, 0), self.text_rect)
        txt = txt + '\nThe dragon was about to step on you when you sneak under him!'
        render_text_centered(txt, self.screen, TEXT_X, TEXT_Y, S_WIDTH)
        yield

        ##############################################################
        # Castle Princess stage
        ##############################################################
        self.valid_text = True
        self.input_text = ''
        self.screen.fill((0,0,0))
        self.bg_castle_princess.draw(self.screen)

        pygame.mixer.music.load('audio/MidnightTale.mp3')
        pygame.mixer.music.play(-1)

        txt = 'You get to the princess and she says "thank you for saving me" with a sparkle in her eye\nDo you wish to return her for the castle or run away and fall in love with her (castle[c] or princess[p]): '
        render_text_centered(txt, self.screen, TEXT_X, TEXT_Y, S_WIDTH)
        valid_text = False
        while not valid_text:
            if not self.input_text:
                yield
            elif self.input_text[0] == 'c':
                self.castle = True
                valid_text = True
            elif self.input_text[0] == 'p':
                self.princess = True
                valid_text = True
            else:
                yield

        ##############################################################
        # Final stage
        ##############################################################
        self.valid_text = True
        self.input_text = ''
        self.screen.fill((0,0,0))
        if self.castle:
            self.bg_victory_castle.draw(self.screen)
            txt = 'You take the princess to the king and he gives you a castle, but it is VERY lonely'
        else:
            self.bg_victory_princess.draw(self.screen)
            txt = 'You get married to the princess, but she complains that you do not have a castle'
        if not self.pinky:
            txt = txt + '\nAND you do not have a pinky'
        render_text_centered(txt, self.screen, TEXT_X, TEXT_Y, S_WIDTH)
        yield

