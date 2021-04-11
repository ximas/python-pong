import pygame
screen=pygame.display.set_mode((800,600))
up=-1000
down=1200
x=100
y=0
angle=-5
while 1:
    file_one='chickenleft.png'
    file_two='chickenright.png'
    c_left=pygame.image.load(file_one)
    c_right=pygame.image.load(file_two)
    if y<down and y>up and angle==-5:      
        y=y+angle
        x=x+angle
        screen.fill((0,0,0))
        screen.blit(c_left,(x,y))
        pygame.display.update()
        screen.fill((0,0,0))
        screen.blit(c_right,(x,y))
        pygame.display.update()
    if y==up:
        y=y+10
        angle=5
    if (y+100)<down and y>up and angle==5:      
        y=y+angle
        x=x+angle
        screen.fill((0,0,0))
        screen.blit(c_left,(x,y))
        pygame.display.update()
        screen.fill((0,0,0))
        screen.blit(c_right,(x,y))
        pygame.display.update()
    if (y+100)==down:
        y=y-10
        angle=-5
