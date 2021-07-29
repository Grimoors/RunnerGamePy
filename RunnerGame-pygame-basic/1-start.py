import pygame
import sys as sys

pygame.init()
screen = pygame.display.set_mode((800,470))
pygame.display.set_caption("Runner UI")
clock = pygame.time.Clock()
test_font= pygame.font.Font('font/Pixeltype.ttf', 30)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load ( 'graphics/ground.png' )
text_surface= test_font.render("Created by : Grimoors",True,'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos=600


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #draw all elements
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(580,430))

    screen.blit(snail_surface,(snail_x_pos,280))
    snail_x_pos-=4
    if(snail_x_pos)<=-100: snail_x_pos=800
    
        
    #update everything
    pygame.display.update()
    clock.tick ( 60 )