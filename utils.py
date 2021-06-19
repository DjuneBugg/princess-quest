import math
import pygame

S_WIDTH = 1200
S_HEIGHT = 800
B_HEIGHT = math.floor(S_HEIGHT*0.75)
B_WIDTH = S_WIDTH
TEXT_X = math.floor(S_WIDTH / 2)
TEXT_Y = B_HEIGHT
INPUT_X = math.floor(S_WIDTH / 2)
INPUT_Y = S_HEIGHT - 75

TEXT_SIZE = 20

class MySurface(pygame.Surface):

    def __init__(self, *args, **kwargs):
        super(pygame.Surface, self).__init__(*args, **kwargs)
        self.change_screen_size(self.get_width(), self.get_height())

    def change_screen_size(self, width, height):
        self.S_WIDTH = width
        self.S_HEIGHT = height
        self.B_WIDTH = self.S_WIDTH
        self.B_HEIGHT = self.S_HEIGHT - 400
        self.TEXT_X = math.floor(self.S_WIDTH / 2)
        self.TEXT_Y = self.B_HEIGHT
        self.INPUT_X = math.floor(self.S_WIDTH / 2)
        self.INPUT_Y = self.S_HEIGHT - 75


def render_text_centered(text, screen, x, y, allowed_width=math.inf, font=None, colour=(255,255,255)):
    # Default font if not provided
    if not font:
        font = pygame.font.SysFont('Comic Sans MS', TEXT_SIZE)

    input_lines = text.splitlines()

    # now, construct lines out of these words
    lines = []
    for input_line in input_lines:
        # split the line into words
        words = input_line.split()

        while len(words) > 0:
            # get as many words as will fit within allowed_width
            line_words = []
            while len(words) > 0:
                word = words.pop(0)
                line_words.append(word)
                fw, fh = font.size(' '.join(line_words + words[:1]))
                if fw > allowed_width or word=='\n':
                    break

            # add a line consisting of those words
            line = ' '.join(line_words)
            lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))
        y_offset += fh
