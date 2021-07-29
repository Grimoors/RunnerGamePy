import pygame
import sys as sys

pygame.init()
screen = pygame.display.set_mode((700,470))
pygame.display.set_caption("Runner UI")
clock = pygame.time.Clock()

sky_surface = pygame.image.load('./graphics/Sky.png')
ground_surface = pygame.image.load ( './graphics/ground.png' )
#//test_surface.fill('ghostwhite')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #draw all elements
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))

    #update everything
    pygame.display.update()
    clock.tick ( 60 )