import math
from typing import *

import pygame

from utils import *

class MySprite(pygame.sprite.Sprite):
    def __init__(self, f_image: str, scale=None):
        super(MySprite, self).__init__()
        image = pygame.image.load(f_image)
        # Scale image if passed in
        if scale:
            image = pygame.transform.scale(image, (scale[0], scale[1]))
        # Rescale image to fit in box
        if image.get_rect().width > B_WIDTH or image.get_rect().height > B_HEIGHT:
            # Scale to match width or height?
            if image.get_rect().width/B_WIDTH > image.get_rect().height/B_HEIGHT:
                tmp_scale = math.floor(image.get_rect().height*B_WIDTH/image.get_rect().width)
                image = pygame.transform.scale(image, (B_WIDTH, tmp_scale))
            else:
                tmp_scale = math.floor(image.get_rect().width*B_HEIGHT/image.get_rect().height)
                image = pygame.transform.scale(image, (tmp_scale, B_HEIGHT))
        self.image = image
        self.rect = image.get_rect()
        # Center image
        self.rect.left = math.floor((B_WIDTH - self.rect.width)/2)
        self.rect.top = math.floor((B_HEIGHT - self.rect.height)/2)
        #self.rect.left, self.rect.top = location

    def draw(self, screen):
        screen.blit(self.image, self.rect)


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
