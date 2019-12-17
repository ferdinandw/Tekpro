#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576
pacicon=pygame.image.load('pacman.png')
bg=pygame.image.load('bgc.jpg')
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Fek Men")
    pygame.display.set_icon(pacicon)
    done = False
    clock = pygame.time.Clock()
    game = Game()
    # Looping Main
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        #30FPS
        clock.tick(30)
        
    pygame.quit()

if __name__ == '__main__':
    main()
