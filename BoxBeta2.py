#pong game------------------------------------------------------------
import pygame
screen=pygame.display.set_mode((800,600))
bat_x=300
bat_y=500
run=1
while run:
    event=pygame.event.poll()
    [m1,m2,m3]=pygame.mouse.get_pressed()
    pygame.display.update()
    if m1==True:
        if bat_x>left and bat_x<(right-200):
            bat_x=bat_x+2
            screen.fill((0,0,0))
            box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
            pygame.display.update()
        if bat_x==left:
            bat_x=bat_x+2
        if bat_x==right:
            bat_x=bat_x-2
    if m3==True:
        if bat_x>left and bat_x<(right-200):
            bat_x=bat_x-2
            screen.fill((0,0,0))
            box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
            pygame.display.update()
        if bat_x==left:
            bat_x=bat_x+2
        if bat_x==right:
            bat_x=bat_x-2
            
            
        

        
