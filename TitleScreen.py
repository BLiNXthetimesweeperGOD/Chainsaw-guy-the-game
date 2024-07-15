import pygame
import sys
import random

WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLEISH = (255, 0, 255)
BLACK = (0, 0, 0)

def title_screen():
    pygame.init()
    screen = pygame.display.set_mode((1300, 600))
    pygame.display.set_caption("Chainsaw Guy")
    font = pygame.font.SysFont("comicsansms", 36)
    text = font.render("Chainsaw Man chops some trees", True, (255, 255, 255))
    text_rect = text.get_rect(center=(650, 300))

    running = True
    pygame.mixer.music.load("Music/TitleScreen.wav")
    pygame.mixer.music.play(-1)
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running = False

        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()
        
title_screen()
