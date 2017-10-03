#! /usr/bin/python3

import pygame

GAME_NAME = "Push into the Pit"
SCREEN_SIZE = (640, 448)
LEVEL_SIZE = (10, 7)
TILE_SIZE = 64

IMAGE_CHAR_UP = pygame.image.load('images/char_up.png')
IMAGE_CHAR_DOWN = pygame.image.load('images/char_down.png')
IMAGE_CHAR_LEFT = pygame.image.load('images/char_left.png')
IMAGE_CHAR_RIGHT = pygame.image.load('images/char_right.png')

IMAGE_BRICK = pygame.image.load('images/brick.png')
IMAGE_FLOOR = pygame.image.load('images/floor.png')
IMAGE_PIT = pygame.image.load('images/pit.png')
IMAGE_BOX = pygame.image.load('images/box.png')
IMAGE_FALL = pygame.image.load('images/fall.png')

IMAGE_START_GAME = pygame.image.load('images/start_game.png')
IMAGE_NEXT = pygame.image.load('images/move_to_next.png')
IMAGE_LEVEL_COMPLETE = pygame.image.load('images/level_complete.png')
IMAGE_RESET_INFO = pygame.image.load('images/reset_info.png')
BG_COLOR = pygame.Color(56, 56, 56)

LEVEL_FILE = 'levels/level'
MAX_LEVELS = 4

TILES = {
            '#' : IMAGE_BRICK,
            '_' : IMAGE_FLOOR,
            '+' : IMAGE_PIT,
            '*' : IMAGE_BOX,
            '@' : IMAGE_FALL,
            '~' : IMAGE_CHAR_UP,
        }
