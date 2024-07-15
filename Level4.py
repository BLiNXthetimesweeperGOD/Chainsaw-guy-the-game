import pygame
import sys
import random

WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLEISH = (255, 0, 255)
BLACK = (0, 0, 0)

collectibles = pygame.sprite.Group()

class Collectible(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("backgrounds/Tree 4.png")
        self.rect = self.image.get_rect()
        self.rect.center = (2500, 300)

def handle_events(world_pos_x, world_pos_y, keys_pressed):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            keys_pressed[event.key] = False
            
def update_score(score):
    score += 1
    return score
    
def update_player_position(world_pos_x, player_direction, keys_pressed):
    speed = 25
    if keys_pressed.get(pygame.K_LEFT):
        world_pos_x -= speed
        player_direction = "right"
    if keys_pressed.get(pygame.K_RIGHT):
        world_pos_x += speed
        player_direction = "left"
    return world_pos_x, player_direction

def Level4():
    pygame.init()
    font = pygame.font.SysFont("comicsansms", 36)
    
    screen = pygame.display.set_mode((1300, 600))
    pygame.display.set_caption("Chainsaw Guy")

    player_pos = [400, 300]
    keys_pressed = {}
    clock = pygame.time.Clock()
    score = 30
    items = 0
    background_image = pygame.image.load("backgrounds/Background4.jpg")
    player_image = pygame.image.load("backgrounds/ChainsawMan.png")
    player_direction = "right"
    bg_rect = background_image.get_rect(center=(400, 0))
    player_rect = player_image.get_rect(center=(400, 300))
    
    base_pos = 140, 100, 100, 220
    flipped_pos = 560, 100, 100, 220
    current = base_pos
    pygame.mixer.music.load("Music/SpaceGameplay.wav")
    pygame.mixer.music.play(-1)

    while True:
        
        visItems = 0
        world_pos_x = 0
        world_pos_y = 0
        
        for collectible in collectibles:
            if collectible.rect.x in range(0, 800):
                visItems+=1

        if random.random() < 0.10 and items < 1 and visItems < 1:
            new_collectible = Collectible()
            collectibles.add(new_collectible)
            
        handle_events(world_pos_x, world_pos_y, keys_pressed)
        world_pos_x, player_direction = update_player_position(world_pos_x, player_direction, keys_pressed)

        screen.blit(background_image, bg_rect)
        
        for collectible in collectibles:
            screen.blit(collectible.image, collectible.rect)
            if world_pos_x != 0:
                collectible.rect.x -= world_pos_x
            if pygame.Rect(current).colliderect(collectible.rect):
                collectible.kill()
                chop_sound = pygame.mixer.Sound("SFX/Chop.wav")
                pygame.mixer.Sound.play(chop_sound)

                score = update_score(score)
            
        items = len(collectibles)
        if player_direction == "left":
            flipped_image = pygame.transform.flip(player_image, True, False)
            screen.blit(flipped_image, player_rect)
            current = flipped_pos
        elif player_direction == "right":
            screen.blit(player_image, player_rect)
            current = base_pos
        
        

        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)
        if score >= 40:
            pygame.display.quit()
            break
Level4()
