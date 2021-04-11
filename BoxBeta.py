import pygame
screen=pygame.display.set_mode((600,600))
a=1
run=1
while run:
    event=pygame.event.poll()
    [m1,m2,m3]=pygame.mouse.get_pressed()
    if m1==True:
        a=a+1
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(0,0,255),(100,a,100,100),0)
        pygame.display.update()
    if m3==True:
        a=a-1
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(0,0,255),(100,a,100,100),0)
        pygame.display.update()
        
