import random
import pygame
import sys
from pygame.locals import *

#global variables
FPS = 60
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'Assets/Gallery/bird.png'
BACKGROUND = 'Assets/Gallery/background.png'
PIPE = 'Assets/Gallery/pipe.png'

def welcomeScreen():
    """
    Show welcome images on screen
    """
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2
    messagex = int(SCREENWIDTH - GAME_SPRITES['message'].get_width())/2
    messagey = int

if __name__ == "__main__":
    #this marks the start of game function
    pygame.init() #intialize pygame
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird")
    GAME_SPRITES['number'] = {
        pygame.image.load('Assets/Gallery/0.png').convert_alpha(),
        pygame.image.load('Assets/Gallery/1.png').convert_alpha(),
        pygame.image.load('Assets/Gallery/2.png').convert_alpha(),
        pygame.image.load('Assets/Gallery/3.png').convert_alpha(),
        pygame.image.load('Assets/Gallery/4.png').convert_alpha(),
        pygame.image.load('Assets/Gallery/5.png').convert_alpha(),
        pygame.image.load('Assets/Gallery/6.png').convert_alpha(),
        pygame.image.load('Assets/Gallery/7.png').convert_alpha(),
        pygame.image.load('Assets/Gallery/8.png').convert_alpha(),
        pygame.image.load('Assets/Gallery/9.png').convert_alpha(),
    }
    
    GAME_SPRITES['message'] = pygame.image.load('Assets/Gallery/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('Assets/Gallery/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()
    )
    
    #game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('Assets/Audio/die.mp3')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('Assets/Audio/hit.mp3')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('Assets/Audio/point.mp3')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('Assets/Audio/Swoosh.mp3')
    GAME_SOUNDS['flap'] = pygame.mixer.Sound('Assets/Audio/flap.mp3')
    
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    
    #game loop
    while True:
        WelcomeScreen() #shows welcome screen until any click is registered
        mainGame() #this is the main game