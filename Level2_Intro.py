import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1300, 600))
pygame.display.set_caption("Chainsaw Guy")
font = pygame.font.Font(None, 36)

text_list = [
    "Wow, the scenery suddenly changed.",
    "It's all cold and snowy out now...",
    "I'm still going to chop down all of the trees!",
    "The cold snow isn't going to stop me!",
    "Here I come!",
    ""
]
pygame.mixer.music.load("Music/IntroCutscene.wav")
pygame.mixer.music.play(-1)
current_text_index = 0
player_image = pygame.image.load("backgrounds/ChainsawMan.png")
x, y = 400, 300
player_rect = player_image.get_rect(center=(x, y))
end = False
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                current_text_index += 1
                if current_text_index >= len(text_list)-1:
                    end = True
                    break

        screen.fill((0, 0, 0))
        if current_text_index < 3:    
            screen.blit(player_image, player_rect)
        if current_text_index == 3:
            flipped_image = pygame.transform.flip(player_image, True, False)
            screen.blit(flipped_image, player_rect)
        if current_text_index == 4:
            flipped_image = pygame.transform.flip(player_image, True, False)
            screen.blit(flipped_image, player_rect)
            player_rect.x += 25
            
        text = font.render(text_list[current_text_index], True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()

        pygame.time.Clock().tick(30)
        if end == True:
            pygame.quit()
            sys.exit()
except:
    "It ended! What a great solution to the problem. Definitely not lazy in any way!"
