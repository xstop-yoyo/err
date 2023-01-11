import pygame, sys

pygame.init()

pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
