import math
from typing import *

import pygame

from utils import *

class MySprite(pygame.sprite.Sprite):
    def __init__(self, f_image: str, scale_box=None):
        """
        Iniitalise a sprite from an image location
        :param f_image:
        :param scale_box: Tuple representing (X, Y, WIDTH, HEIGHT) of box to scale and place image in
        """
        super(MySprite, self).__init__()
        image = pygame.image.load(f_image)
        # Scale image to box if passed in
        if scale_box:
            scale_x = scale_box[0]
            scale_y = scale_box[1]
            scale_width = scale_box[2]
            scale_height = scale_box[3]
        else:
            scale_x = 0
            scale_y = 0
            scale_width = B_WIDTH
            scale_height = B_HEIGHT
        # Rescale image to fit in box
        if image.get_rect().width > scale_width or image.get_rect().height > scale_height:
            # Scale to match width or height?
            if image.get_rect().width/scale_width > image.get_rect().height/scale_height:
                tmp_scale = math.floor(image.get_rect().height*scale_width/image.get_rect().width)
                image = pygame.transform.scale(image, (scale_width, tmp_scale))
            else:
                tmp_scale = math.floor(image.get_rect().width*scale_height/image.get_rect().height)
                image = pygame.transform.scale(image, (tmp_scale, scale_height))
        self.image = image
        self.rect = image.get_rect()
        # Center image
        self.rect.left = scale_x + math.floor((scale_width - self.rect.width)/2)
        self.rect.top = scale_y + math.floor((scale_height - self.rect.height)/2)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def set_location(self, x, y):
        self.rect.left = x
        self.rect.top = y

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, f_images: List, scale=None):
        super(AnimatedSprite, self).__init__()
        self.images = []
        for f in f_images:
            image = pygame.image.load(f)
            # Scale image if passed in
            if scale:
                image = pygame.transform.scale(image, (scale[0], scale[1]))
            self.images.append(image)
            self.rect = image.get_rect()

        self.index = 0
        self.image = self.images[self.index]
        #self.rect.left, self.rect.top = location

    def update(self):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
