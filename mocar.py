#import packages
import pygame
import time
import random
#intialize pygame
pygame.init()
#declare some variables value
gray=(119,118,110)
white=(255,255,255)
cyan=(0,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
display_width=1080
display_height=1000

#define screen

gamedisplays=pygame.display.set_mode((display_width,display_height))
#call clock function
clock=pygame.time.Clock()
#load images
carimg=pygame.image.load('car1.jpg')
backgroundpic=pygame.image.load("grass.jpg")
yellow_strip=pygame.image.load("yellow_strip.jpg")
strip=pygame.image.load("strip.jpg")
strip2=pygame.image.load("strip2.jpg")
intro_background=pygame.image.load("bgg.jpg")
instruction_background=pygame.image.load("bggg.jpg")
car_width=56
pause=False
#introduction page function
def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("CAR GAME",largetext)
        TextRect.center=(500,100)
        gamedisplays.blit(TextSurf,TextRect)
        button("START",150,1000,100,50,green,bright_green,"play")
        button("QUIT",450,1000,100,50,red,bright_red,"quit")
        button("HELP",300,1000,100,50,white,cyan,"intro")
        pygame.display.update()
        clock.tick(50)

# function to create rectangle shaped button
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()


    else:
        pygame.draw.rect(gamedisplays,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)
    
'''def circular(msg,xc,x,y,r,ac,ic,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+r>mouse[0]>x and y+r>mouse[1]>y:
        pygame.draw.circle(gamedisplays,ac,(x,y),r)
        if click[0]==1 and action!=None:
            if action=="left":
                xc=-5
            elif action=="right":
                
                xc=5
                
            elif action==None:
                xc=0
  


    else:
        pygame.draw.circle(gamedisplays,ic,(x,y),r)
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x),(y))
    gamedisplays.blit(textsurf,textrect)
    '''


#function to create help page instructions

def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects(" you need cross the coming cars",smalltext)
        textRect.center=((350),(300))
        TextSurf,TextRect=text_objects("HELP",largetext)
        TextRect.center=((500),(200))
        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("l : LEFT TURN",smalltext)
        stextRect.center=((150),(500))
        hTextSurf,hTextRect=text_objects("r : RIGHT TURN" ,smalltext)
        hTextRect.center=((150),(550))
        nTextSurf,nTextRect=text_objects(" n : NO TURN" ,smalltext)
        nTextRect.center=((150),(600))
        atextSurf,atextRect=text_objects("A : ACCELERATOR",smalltext)
        atextRect.center=((150),(650))
        rtextSurf,rtextRect=text_objects("B : BRAKE ",smalltext)
        rtextRect.center=((150),(700))
        ptextSurf,ptextRect=text_objects("P : PAUSE  ",smalltext)
        ptextRect.center=((150),(750))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((250),(400))
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(stextSurf,stextRect)
        gamedisplays.blit(hTextSurf,hTextRect)
        gamedisplays.blit(nTextSurf,nTextRect)
        gamedisplays.blit(atextSurf,atextRect)
        gamedisplays.blit(rtextSurf,rtextRect)
        gamedisplays.blit(ptextSurf,ptextRect)
        button("BACK",600,550,100,50,white,cyan,"menu")
        pygame.display.update()
        clock.tick(30)
#pause function for getting another page with continue,restart ,menu button
def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.blit(instruction_background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            button("CONTINUE",150,1080,150,50,green,bright_green,"unpause")
            button("RESTART",350,1080,150,50,cyan,bright_blue,"play")
            button("MAIN MENU",550,1080,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)
#to define unpause event 
def unpaused():
    global pause
    pause=False

#to show countdown background
def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(display_width/2)
    y=(display_height)
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(960,0))
    gamedisplays.blit(yellow_strip,(540,18))
    gamedisplays.blit(yellow_strip,(540,100))
    gamedisplays.blit(yellow_strip,(540,200))
    gamedisplays.blit(yellow_strip,(540,300))
    gamedisplays.blit(yellow_strip,(540,400))
    gamedisplays.blit(yellow_strip,(540,500))
    gamedisplays.blit(yellow_strip,(540,600))
    gamedisplays.blit(yellow_strip,(540,700))
    gamedisplays.blit(yellow_strip,(540,800))
    gamedisplays.blit(yellow_strip,(540,900))
    
    gamedisplays.blit(strip,(150,0))
    gamedisplays.blit(strip,(940,0))
    gamedisplays.blit(strip2,(150,800))
    gamedisplays.blit(strip2,(940,800))
    
    
    gamedisplays.blit(carimg,(x,y))
    text=font.render("DODGED: 0",True, black)
    score=font.render("SCORE: 0",True,red)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))
    button("PAUSE",790,1,120,40,cyan,white,"pause")
#to show countdown after start
def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("GO!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()
#define enemie cars moving opposite
def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("car1.jpg")
    elif obs==1:
        obs_pic=pygame.image.load("car3.jpg")
    elif obs==2:
        obs_pic=pygame.image.load("car2.png")
    elif obs==3:
        obs_pic=pygame.image.load("car4.jpg")
    elif obs==4:
        obs_pic=pygame.image.load("car5.jpg")
    elif obs==5:
        obs_pic=pygame.image.load("car6.jpg")
    elif obs==6:
        obs_pic=pygame.image.load("car7.jpg")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))
#to show score and car passed
def score_system(passed,score):
    font=pygame.font.SysFont(None,30)
    text=font.render("Passed"+str(passed),True,black)
    score=font.render("Score"+str(score),True,red)
    gamedisplays.blit(text,(1,50))
    gamedisplays.blit(score,(1,30))

#to add text on screen or buttons
def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()
#display message on screen 
def message_display(text):
    largetext=pygame.font.SysFont("NONE",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("YOU CRASHED")

#to show car on screen
def car(x,y):
    gamedisplays.blit(carimg,(x,y))
#game page
def game_loop():
    global pause
    x=(display_width/2)
    y=(display_height)
    x_change=0
    obstacle_speed=9
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-130
    obs_width=56
    obs_height=125
    passed=0
    level=0
    score=0
    y2=0
    
    
#to move car in x-y direction
    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_l:
                    x_change=-5
                if event.key==pygame.K_r:
                    x_change=5
                if event.key==pygame.K_a:
                    obstacle_speed+=2
                if event.key==pygame.K_b:
                    obstacle_speed-=2
                if event.key==pygame.K_n:
                    x_change=0

        x+=x_change
        pause=True
        gamedisplays.fill(gray)
        
        
    #to move background with car speed to make real    
        rel_y=y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic,(960,rel_y-backgroundpic.get_rect().width))
        if rel_y<1000:
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(960,rel_y))
            gamedisplays.blit(yellow_strip,(540,rel_y))
            gamedisplays.blit(yellow_strip,(540,rel_y+100))
            gamedisplays.blit(yellow_strip,(540,rel_y+200))
            gamedisplays.blit(yellow_strip,(540,rel_y+300))
            gamedisplays.blit(yellow_strip,(540,rel_y+400))
            gamedisplays.blit(yellow_strip,(540,rel_y+500))
            gamedisplays.blit(yellow_strip,(540,rel_y+600))
            gamedisplays.blit(yellow_strip,(540,rel_y+700))
            gamedisplays.blit(yellow_strip,(540,rel_y+800))
            gamedisplays.blit(yellow_strip,(540,rel_y+900))
            
            gamedisplays.blit(yellow_strip,(540,rel_y-100))
            gamedisplays.blit(strip,(150,rel_y-100))
            gamedisplays.blit(strip,(150,rel_y+200))
         
            gamedisplays.blit(strip,(940,rel_y-100))
            gamedisplays.blit(strip,(940,rel_y+200))
          
            '''circular("L",x_change,110,600,50,whit,cyan,"left")
             circular("R",x_change,810,600,50,white,cyan,"right")'''
            
  
            
            

     
        y2+=obstacle_speed
       # x+=x_change


# ensure enemy car movement
#if enemy cars touch car from left or right then crash message display

        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score)
        if x>940-car_width or x<108+car_width:
            crash()
        
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,7)
            
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level=level+1
                obstacle_speed+2
                largetext=pygame.font.Font("freesansbold.ttf",80)
                textsurf,textrect=text_objects("LEVEL"+str(level),largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(3)
#if enemy cars touch car from front ,crash message display

        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()
                #pause bitton dimensions
        button("PAUSE",790,1,120,40,cyan,white,"pause")
        #screen update with all these effects
        pygame.display.update()
        clock.tick(60)
intro_loop()# firstly introduction page open then on pressing 
game_loop()# game loop function starts
pygame.quit()# quit button pressed pygame display close
