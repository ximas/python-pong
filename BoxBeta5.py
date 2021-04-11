#pong game------------------------------------------------------------
import pygame
import pickle
screen=pygame.display.set_mode((800,600))
#functions--------------------------------------------------------------------
#menu-------------------------------------------------------------------------
def menu():
    run=1
    screen.fill((0,0,0))
    while run==1:
        pygame.draw.rect(screen,(255,0,0),(100,100,200,100),0)
        pygame.draw.rect(screen,(0,255,0),(100,400,200,100),0)
        pygame.draw.rect(screen,(0,0,255),(500,100,200,100),0)
        pygame.draw.rect(screen,(255,0,255),(500,400,200,100),0)
        pygame.display.update()
        event=pygame.event.poll()
        mouse_down=pygame.MOUSEBUTTONDOWN
        [mouse_x,mouse_y]=pygame.mouse.get_pos()
        if event.type==mouse_down:
            if mouse_x>100 and mouse_x<300 and mouse_y>100 and mouse_y<200:
                one_player
            if mouse_x>500 and mouse_x<700 and mouse_y>100 and mouse_y<200:
               this_run=2
               return this_run
def append(points):
    point.append(points)
def p1point(points,run,run2):
    if points<30:
        points=points+15
        run2=0
    if points==30:
        run2=0
        points=points+10
    if points==40:
        run2=0
        points==points+10
    if points==50:
        run=0
    return [run2,run,points]
def p2point(points,run,run2):
    if points<30:
        points=points+15
        run2=0
    if points==30:
        points=points+10
        run2=0
    if points==40:
        points==points+10
        run2=0
    if points==50:
        run2=0
        run=0
    return [run2,run,points]
#oneplayer mode---------------------------------------------------------------
#-----------------------------------------------------------------------------------
def one_player():
    while run==1:
        left=0
        down=600
        right=800
        up=0
        option=1
        ball_x=400
        ball_y=0
        bat_x=300
        bat_y=500
        p1bat_x=50
        p1bat_y=200
        p2bat_x=700
        p2bat_y=200
        points=0
        p1points=0
        p2points=0
        point=[]
#ball----------------------------------------------------------------------------
        if option==1:       
            ball_x=ball_x+4
            ball_y=ball_y+4
            screen.fill((0,0,0))
            box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
            ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
            pygame.display.update()
        if option==2:       
            ball_x=ball_x+4
            ball_y=ball_y-4
            screen.fill((0,0,0))
            box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
            ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
            pygame.display.update()
        if option==3:       
            ball_x=ball_x-4
            ball_y=ball_y-4
            screen.fill((0,0,0))
            box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
            ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
            pygame.display.update()
        if option==4:       
            ball_x=ball_x-4
            ball_y=ball_y+4
            screen.fill((0,0,0))
            box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)        
            ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
            pygame.display.update()
    #option changes-------------------------------------------------------------
        if ball_y==(down-100) and option==1 and (bat_x+200)>ball_x and bat_x<ball_x :
            option=2
            points=points+10
        if ball_x==right and option==2:
            option=3
        if ball_y==up and option==3:
            option=4
        if ball_y==(down-100) and option==4 and (bat_x+200)>ball_x and bat_x<ball_x:
            option=3
            points=points+10
        if ball_x==left and option==3:
            option=2
        if ball_y==up and option==2:
            option=1
        if ball_x==right and option==1:
            option=4
        if ball_x==left and option==4:
            option=1
        if ball_y>down:
            print("You got: ",points)
            append(points)
            run=0
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

    
    
    

#variables-------------------------------------------------------------------
main_run=1
#main--------------------------------------------------------------------------
while main_run==1:
    run=menu()
#one player-----------------------------------------------------------------------
#ball-----------------------------------------------------------------------------
    
    #2 player--------------------------------------------------------------------------
#------------------------------------------------------------------------------------
    while run==2:
        left=0
        down=600
        right=800
        up=0
        option=1
        ball_x=300
        ball_y=0
        p1bat_x=150
        p1bat_y=200
        p2bat_x=600
        p2bat_y=200
        p1points=0
        p2points=0
        run2=1
        while run2==1:
            if p1points==15:
                pygame.draw.circle(screen,(255,255,0),(10,10),10,0)
                pygame.display.update()
            if p1points==30:
                pygame.draw.circle(screen,(255,255,0),(10,10),10,0)
                pygame.draw.circle(screen,(255,255,0),(30,10),10,0)
                pygame.display.update()
            if p1points==40:
                pygame.draw.circle(screen,(255,255,0),(10,10),10,0)
                pygame.draw.circle(screen,(255,255,0),(30,10),10,0)
                pygame.draw.circle(screen,(255,255,0),(50,10),10,0)
                pygame.display.update()
            if p2points==15:
                pygame.draw.circle(screen,(255,255,0),(780,10),10,0)
                pygame.display.update()
            if p2points==30:
                pygame.draw.circle(screen,(255,255,0),(780,10),10,0)
                pygame.draw.circle(screen,(255,255,0),(760,10),10,0)
                pygame.display.update()
            if p2points==40:
                pygame.draw.circle(screen,(255,255,0),(780,10),10,0)
                pygame.draw.circle(screen,(255,255,0),(760,10),10,0)
                pygame.draw.circle(screen,(255,255,0),(740,10),10,0)
                pygame.display.update()
            if option==1:       
                ball_x=ball_x+4
                ball_y=ball_y+4
                screen.fill((0,0,0))
                box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                pygame.display.update()
            if option==2:       
                ball_x=ball_x+4
                ball_y=ball_y-4
                screen.fill((0,0,0))
                box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                pygame.display.update()
            if option==3:       
                ball_x=ball_x-4
                ball_y=ball_y-4
                screen.fill((0,0,0))
                box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                pygame.display.update()
            if option==4:       
                ball_x=ball_x-4
                ball_y=ball_y+4
                screen.fill((0,0,0))
                box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)        
                ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                pygame.display.update()
#option changes-------------------------------------------------------------
            if ball_y==down and option==1:
                option=2
            if ball_x==(right-200) and option==2 and p2bat_y<ball_y and (p2bat_y+200)>ball_y:
                option=3
            if ball_y==up and option==3:
                option=4
            if ball_y==down and option==4:
                option=3
            if ball_x==(left+200) and option==3 and p1bat_y<ball_y and (p1bat_y+200)>ball_y:
                option=2
            if ball_y==up and option==2:
                option=1
            if ball_x==(right-200) and option==1 and p2bat_y<ball_y and (p2bat_y+200)>ball_y:
                option=4
            if ball_x==(left+200) and option==4 and p1bat_y<ball_y and (p1bat_y+200)>ball_y:
                option=1
            if ball_x<left:
                [run2,run,p2points]=p2point(p2points,run,run2)
            if ball_x>right:
                [run2,run,p1points]=p1point(p1points,run,run2)
                
#bat 1---------------------------------------------------------------------------
            event=pygame.event.poll()
            pygame.event.pump()
            key_pressed=pygame.key.get_pressed()
            Kw=pygame.K_w
            Ks=pygame.K_s
            pygame.display.update()
            if key_pressed[Ks]:
                if p1bat_y>up and p1bat_y<(down-200):
                    p1bat_y=p1bat_y+2
                    screen.fill((0,0,0))
                    ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                    box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                    box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                    pygame.display.update()
                if p1bat_y==up:
                    p1bat_y=p1bat_y+2
                if p1bat_y==(down-200):
                    p1bat_y=p1bat_y-2
            if key_pressed[Kw]:
                if p1bat_y>up and p1bat_y<(down-200):
                    p1bat_y=p1bat_y-2
                    screen.fill((0,0,0))
                    ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                    box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                    box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                    pygame.display.update()
                if p1bat_y==up:
                    p1bat_y=p1bat_y+2
                if p1bat_y==(down-200):
                    p1bat_y=p1bat_y-2
#bat2-----------------------------------------------------------------------------------
            event=pygame.event.poll()
            [m1,m2,m3]=pygame.mouse.get_pressed()
            pygame.display.update()
            if m1==True:
                if p2bat_y>up and p2bat_y<(down-200):
                    p2bat_y=p2bat_y+2
                    screen.fill((0,0,0))
                    ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                    box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                    box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                    pygame.display.update()
                if p2bat_y==up:
                    p2bat_y=p2bat_y+2
                if p2bat_y==(down-200):
                    p2bat_y=p2bat_y-2
            if m3==True:
                if p2bat_y>up and p2bat_y<(down-200):
                    p2bat_y=p2bat_y-2
                    screen.fill((0,0,0))
                    ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                    box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                    box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                    pygame.display.update()
                if p2bat_y==up:
                    p2bat_y=p2bat_y+2
                if p2bat_y==(down-200):
                    p2bat_y=p2bat_y-2
#points-----------------------------------------------------------------------------------
