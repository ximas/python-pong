#pong game------------------------------------------------------------
import pygame
screen=pygame.display.set_mode((800,600))

#functions--------------------------------------------------------------------
#--------------------------------------------------------------------------------
#menu function-------------------------------------------------------------
def menu(screen,on,chk):
    run=1
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
                [on,chk]=Option(on,chk)
                one_player(on)
                run=0
            if mouse_x>500 and mouse_x<700 and mouse_y>100 and mouse_y<200:
                two_player()
                run=0
    return [on,chk]
#adds 1player score to the list to save scores---------------------------------            
def append(points,point):
    point.append(points)
#draws the point on 2 player----------------------------------------------------
def draw_points(p1,p2):
    if p1==10:
        pygame.draw.circle(screen,(255,0,255),(10,10),10,0)
    if p1==20:
        pygame.draw.circle(screen,(255,0,255),(10,10),10,0)
        pygame.draw.circle(screen,(255,0,255),(30,10),10,0)
    if p1==30:
        pygame.draw.circle(screen,(255,0,255),(10,10),10,0)
        pygame.draw.circle(screen,(255,0,255),(30,10),10,0)
        pygame.draw.circle(screen,(255,0,255),(50,10),10,0)
    if p1==40:
        pygame.draw.circle(screen,(255,0,255),(10,10),10,0)
        pygame.draw.circle(screen,(255,0,255),(30,10),10,0)
        pygame.draw.circle(screen,(255,0,255),(50,10),10,0)
        pygame.draw.circle(screen,(255,0,255),(70,10),10,0)
    if p2==10:
        pygame.draw.circle(screen,(255,0,255),(780,10),10,0)
    if p2==20:
        pygame.draw.circle(screen,(255,0,255),(780,10),10,0)
        pygame.draw.circle(screen,(255,0,255),(760,10),10,0)
    if p2==30:
        pygame.draw.circle(screen,(255,0,255),(780,10),10,0)
        pygame.draw.circle(screen,(255,0,255),(760,10),10,0)
        pygame.draw.circle(screen,(255,0,255),(740,10),10,0)
    if p2==40:
        pygame.draw.circle(screen,(255,0,255),(780,10),10,0)
        pygame.draw.circle(screen,(255,0,255),(760,10),10,0)
        pygame.draw.circle(screen,(255,0,255),(740,10),10,0)
        pygame.draw.circle(screen,(255,0,255),(720,10),10,0)
    pygame.display.update()
    
        
#checks the 2player scores to see who won------------------------------
def check_scores(p1,p2):
    if p1==40:
        print("Player one got: ", p1, " points.")
        print("Player two got: ", p2, " points.")
        print("Player one wins!!!")
        run=0
        return run
    if p2==40:
        print("Player one got: ", p1, " points.")
        print("Player two got: ", p2, " points.")
        print("Player two wins!!!")
        run=0
        return run
    else:
        run=1
        return run
#makes one player unpredictable----------------------------------------
def Option(start,chk):
    if chk==0:
        start=1
        chk=1
    if chk==1:
        start=1
        chk=1
    if start==1 and chk==2:
        start=4
    if start==4 and chk==3:
        start=1
    chk=chk+1
    if chk>2:
        chk=1
    return [start,chk]
    
#oneplayer mode--------------------------------------------------------------
#-----------------------------------------------------------------------------------
def one_player(start):
    left=0
    down=600
    right=800
    up=0
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
    main_run=1
    while main_run==1:
#click to start-----------------------------------------------------------------
        screen.fill((0,0,0))
        box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
        ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
        pygame.display.update()
        event=pygame.event.poll()
        mouse_down=pygame.MOUSEBUTTONDOWN
        if event.type==mouse_down:
            run=1
            option=start
            while run==1:
        #ball----------------------------------------------------------------------------
                if option==1:       
                    ball_x=ball_x+1
                    ball_y=ball_y+1
                    screen.fill((0,0,0))
                    box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
                    ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                    pygame.display.update()
                if option==2:       
                    ball_x=ball_x+1
                    ball_y=ball_y-1
                    screen.fill((0,0,0))
                    box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
                    ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                    pygame.display.update()
                if option==3:       
                    ball_x=ball_x-1
                    ball_y=ball_y-1
                    screen.fill((0,0,0))
                    box=pygame.draw.rect(screen,(0,0,255),(bat_x,bat_y,200,50),0)
                    ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                    pygame.display.update()
                if option==4:       
                    ball_x=ball_x-1
                    ball_y=ball_y+1
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
                    append(points,point)
                    run=0
    #bat---------------------------------------------------------------------------
                event=pygame.event.poll()
                [m1,m2,m3]=pygame.mouse.get_pressed()
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
            if run==0:
                main_run=0

#-----------------------------------------------------------------------------------
#twoplayer mode--------------------------------------------------------------
#-----------------------------------------------------------------------------------
def two_player():
    run=1
    p1points=0
    p2points=0
    while run==1:
        file_one='chickenleft.png'
        file_two='chickenright.png'
        c_left=pygame.image.load(file_one)
        c_right=pygame.image.load(file_two)
        left=0
        down=600
        right=800
        up=0
        ball_x=300
        ball_y=0
        p1bat_x=150
        p1bat_y=200
        p2bat_x=600
        p2bat_y=200
        run2=1
        c_up=-1000
        c_down=1200
        c_x=-500
        c_y=-500
        angle=-5
        option=1
        while run2==1:
            if option==1:       
                ball_x=ball_x+4
                ball_y=ball_y+4
                screen.fill((0,0,0))
                box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                screen.blit(c_left,(c_x,c_y))
                screen.blit(c_right,(c_x,c_y))
                pygame.display.update()
            if option==2:       
                ball_x=ball_x+4
                ball_y=ball_y-4
                screen.fill((0,0,0))
                box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                screen.blit(c_left,(c_x,c_y))
                screen.blit(c_right,(c_x,c_y))
                pygame.display.update()
            if option==3:       
                ball_x=ball_x-4
                ball_y=ball_y-4
                screen.fill((0,0,0))
                box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                screen.blit(c_left,(c_x,c_y))
                screen.blit(c_right,(c_x,c_y))
                pygame.display.update()
            if option==4:       
                ball_x=ball_x-4
                ball_y=ball_y+4
                screen.fill((0,0,0))
                box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)        
                ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                screen.blit(c_left,(c_x,c_y))
                screen.blit(c_right,(c_x,c_y))
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
                p2points=p2points+10
                run2=0
            if ball_x>right:
                p1points=p1points+10
                run2=0
#random chicken-------------------------------------------------------------
            if c_y<c_down and c_y>c_up and angle==-5:      
                c_y=c_y+angle
                c_x=c_x+angle
                screen.fill((0,0,0))
                screen.blit(c_left,(c_x,c_y))
##                pygame.display.update()
                screen.fill((0,0,0))
                screen.blit(c_right,(c_x,c_y))
##                pygame.display.update()
                box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                pygame.display.update()
            if c_y==c_up:
                c_y=c_y+10
                angle=5
            if (c_y+100)<c_down and c_y>c_up and angle==5:      
                c_y=c_y+angle
                c_x=c_x+angle
                screen.fill((0,0,0))
                screen.blit(c_left,(c_x,c_y))
##                pygame.display.update()
                screen.fill((0,0,0))
                screen.blit(c_right,(c_x,c_y))
##                pygame.display.update()
                box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                pygame.display.update()
            if (c_y+100)==c_down:
                c_y=c_y-10
                angle=-5
#bat 1---------------------------------------------------------------------------
            event=pygame.event.poll()
            pygame.event.pump()
            key_pressed=pygame.key.get_pressed()
            Kw=pygame.K_w
            Ks=pygame.K_s
            if key_pressed[Ks]:
                if p1bat_y>up and p1bat_y<(down-200):
                    p1bat_y=p1bat_y+2
                    screen.fill((0,0,0))
                    ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                    box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                    box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                    screen.blit(c_left,(c_x,c_y))
                    screen.blit(c_right,(c_x,c_y))
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
                    screen.blit(c_left,(c_x,c_y))
                    screen.blit(c_right,(c_x,c_y))
                    pygame.display.update()
                if p1bat_y==up:
                    p1bat_y=p1bat_y+2
                if p1bat_y==(down-200):
                    p1bat_y=p1bat_y-2
#bat2-----------------------------------------------------------------------------------
            event=pygame.event.poll()
            [m1,m2,m3]=pygame.mouse.get_pressed()
            if m1==True:
                if p2bat_y>up and p2bat_y<(down-200):
                    p2bat_y=p2bat_y+2
                    screen.fill((0,0,0))
                    ball=pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),10,0)
                    box2=pygame.draw.rect(screen,(0,255,0),(p2bat_x,p2bat_y,50,200),0)
                    box=pygame.draw.rect(screen,(0,0,255),(p1bat_x,p1bat_y,50,200),0)
                    screen.blit(c_left,(c_x,c_y))
                    screen.blit(c_right,(c_x,c_y))
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
                    screen.blit(c_left,(c_x,c_y))
                    screen.blit(c_right,(c_x,c_y))
                    pygame.display.update()
                if p2bat_y==up:
                    p2bat_y=p2bat_y+2
                if p2bat_y==(down-200):
                    p2bat_y=p2bat_y-2
            run=check_scores(p1points,p2points)
            draw_points(p1points,p2points)
            pygame.display.update()
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
    

    
#variables-------------------------------------------------------------------------
main_run=1
on=0
chk=0
#main------------------------------------------------------------------------------
while main_run==1:
    screen.fill((0,0,0))
    pygame.display.update
    [on,chk]=menu(screen,on,chk)
    
