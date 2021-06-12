import math
import pygame

S_WIDTH = 1500
S_HEIGHT = 1000
B_WIDTH = 1500
B_HEIGHT = 800
TEXT_X = S_WIDTH/2
TEXT_Y = 800
INPUT_X = 700
INPUT_Y = 900


def render_text_centered(text, screen, x, y, allowed_width=math.inf, font=None, colour=(255,255,255)):
    # Default font if not provided
    if not font:
        font = pygame.font.SysFont('Comic Sans MS', 30)

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
