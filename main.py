import pygame, sys

pygame.init()

####################
#  B O B   B O B
Bob_surf = pygame.image.load("Images/Bob.png")
Bob_rect = Bob_surf.get_rect()
#  B O B   B O B
####################

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game")
pygame.display.set_icon(Bob_surf)

Player_surf = pygame.image.load("Images/Player.png").convert_alpha()
Player_rect = Player_surf.get_rect(center=(screen.get_width()/2, screen.get_height()/2))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0, 0, 0))
    screen.blit(Player_surf, Player_rect)

    clock.tick(60)
