#pong game------------------------------------------------------------
import pygame
screen=pygame.display.set_mode((800,600))
left=0
down=500
right=800
up=0
option=1
ball_x=0
ball_y=0
bat_x=300
bat_y=500
run=1
#main--------------------------------------------------------------------------
while run:
#ball-----------------------------------------------------------------------------
    if option==1:       
        ball_x=ball_x+2
        ball_y=ball_y+2
        screen.fill((0,0,0))
        box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
        ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
        pygame.display.update()
    if option==2:       
        ball_x=ball_x+2
        ball_y=ball_y-2
        screen.fill((0,0,0))
        box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
        ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
        pygame.display.update()
    if option==3:       
        ball_x=ball_x-2
        ball_y=ball_y-2
        screen.fill((0,0,0))
        box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
        ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
        pygame.display.update()
    if option==4:       
        ball_x=ball_x-2
        ball_y=ball_y+2
        screen.fill((0,0,0))
        box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)        
        ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
        pygame.display.update()
#option changes-------------------------------------------------------------
    if ball_y==down and option==1 and (bat_x+200)>ball_x and bat_x<ball_x :
        option=2
    if ball_x==right and option==2:
        option=3
    if ball_y==up and option==3:
        option=4
    if ball_y==down and option==4 and (bat_x+200)>ball_x and bat_x<ball_x:
        option=3
    if ball_x==left and option==3:
        option=2
    if ball_y==up and option==2:
        option=1
    if ball_x==right and option==1:
        option=4
    if ball_x==left and option==4:
        option=1
#bat---------------------------------------------------------------------------
    event=pygame.event.poll()
    [m1,m2,m3]=pygame.mouse.get_pressed()
    pygame.display.update()
    if m1==True:
        if bat_x>left and bat_x<(right-200):
            bat_x=bat_x+2
            screen.fill((0,0,0))
            ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
            box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
            pygame.display.update()
        if bat_x==left:
            bat_x=bat_x+2
        if bat_x==(right-200):
            bat_x=bat_x-2
    if m3==True:
        if bat_x>left and bat_x<(right-200):
            bat_x=bat_x-2
            screen.fill((0,0,0))
            ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
            box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
            pygame.display.update()
        if bat_x==left:
            bat_x=bat_x+2
        if bat_x==(right-200):
            bat_x=bat_x-2
