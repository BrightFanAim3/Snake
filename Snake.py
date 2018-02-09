import pygame,sys,time,random
from pygame.locals import *
pygame.init()
fps=pygame.time.Clock()
surface=pygame.display.set_mode((900,640))
pygame.display.set_caption('Python Wanna to Eat') #init the window
pygame.display.set_icon(pygame.image.load('icon.png'))

pygame.mixer.music.load("background.ogg")
pygame.mixer.music.play(-1,0)

ColorRed=pygame.Color(255,0,0)
ColorBlack=pygame.Color(0,0,0)
ColorWhite=pygame.Color(255,255,255)
ColorGrey=pygame.Color(130,130,130)
ColorGreen=pygame.Color(0,255,0)
effect = pygame.mixer.Sound("effect.wav")
SideLabel = pygame.image.load("sidelabel.png").convert_alpha()
Bimage = pygame.image.load("bg.png").convert_alpha()
fpsset=10
global CMode
CMode = True
# init the basic colors
global Score
Score=0
global HighScore
HighScore = 0
def CaMode():
    global CMode
    ScoreFont = pygame.font.Font('freesansbold.ttf', 32)
    global ScoreSurf3
    ScoreSurf3 = ScoreFont.render('Challenge' + "  " + 'ON', True, ColorBlack)
    if CMode==True:
        ScoreSurf3 = ScoreFont.render('Challenge' + "  " + 'ON', True, ColorBlack)
    if CMode==False:
        ScoreSurf3 = ScoreFont.render('Challenge' + "  " + 'OFF', True, ColorBlack)
    ScoreRect3 = ScoreSurf3.get_rect()
    ScoreRect3.topleft = (645, 130)
    surface.blit(ScoreSurf3, ScoreRect3)
def Challenge():
    global CMode
    global Score
    global fpsset
    if CMode == True:
        if Score >=100:
            fpsset = int(round(Score/100))+10
def HighScoreFunc():
    f = open("Score", "r")
    lines = f.read()
    f.close()
    global HighScore
    if int(lines)>=HighScore:
        HighScore=int(lines)
    global Score
    if Score >= HighScore:
        f = open("Score", "w")
        HighScore=Score
        f.write(str(HighScore))
        f.close()
def Sound():
    effect.play()
def GameOver():
        a=75
        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key==K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))
            if a <= 0:
                startgame()
            surface.blit(Bimage, (0, 0))
            GameOverFont = pygame.font.Font('freesansbold.ttf', 72)
            GameOverSurf = GameOverFont.render('--You Failed--', True, ColorRed)
            GameOverRect = GameOverSurf.get_rect()
            GameOverRect.midtop = (320, 10)
            surface.blit(GameOverSurf, GameOverRect)
            GameOverSurf3 = GameOverFont.render('Game Will Restart', True, ColorRed)
            GameOverRect3 = GameOverSurf3.get_rect()
            GameOverRect3.midtop = (320, 120)
            surface.blit(GameOverSurf3, GameOverRect3)
            GameOverSurf4 = GameOverFont.render('At '+str(round(a/15))+' Seconds', True, ColorRed)
            GameOverRect4 = GameOverSurf4.get_rect()
            GameOverRect4.midtop = (320, 230)
            surface.blit(GameOverSurf4, GameOverRect4)
            pygame.draw.rect(surface, ColorGrey, Rect(640, 0, 360, 640))
            surface.blit(SideLabel, (640, 0))
            ScoreFont = pygame.font.Font('freesansbold.ttf', 32)
            global Score
            HighScoreFunc()
            ScoreSurf = ScoreFont.render('Finnal ' + str(Score), True, ColorRed)
            ScoreRect = ScoreSurf.get_rect()
            ScoreRect.topleft = (645, 10)
            ScoreSurf2 = ScoreFont.render('HighScore' + "  " + str(HighScore), True, ColorRed)
            ScoreRect2 = ScoreSurf2.get_rect()
            ScoreRect2.topleft = (645, 70)
            surface.blit(ScoreSurf, ScoreRect)
            surface.blit(ScoreSurf2, ScoreRect2)
            fps.tick(15)
            a-=1
            pygame.display.flip()
            #Set Game Over Menu

def startgame():
        global CMode
        global fpsset
        fpsset = 10
        HighScoreFunc()
        HeadPosition=[100,100]
        SegmentsPosition=[[100,100],[80,80],[60,100]]
        FoodPosition=[300,300]
        FoodSpawned=1
        Direction='right'
        ChangeDirection=Direction #spawn the python's body and food
        Playing = True
        Busy=False
        Music=True
        while Playing == True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==KEYDOWN:
                    if event.key==K_RIGHT or event.key==ord('d'):
                        ChangeDirection='right'
                    if event.key==K_LEFT or event.key==ord('a'):
                        ChangeDirection='left'
                    if event.key==K_UP or event.key==ord('w'):
                        ChangeDirection='up'
                    if event.key==K_DOWN or event.key==ord('s'):
                        ChangeDirection='down'
                    if event.key==K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))
                    if event.key==ord('z'):
                        if fpsset>5:
                            fpsset-=5
                            fps.tick(fpsset)
                    if event.key==ord('x'):
                        if fpsset<35:
                            fpsset+=5
                            fps.tick(fpsset)
                    if event.key==ord('c'):
                        if CMode == True:
                           CMode = False
                           CaMode()
                           pygame.display.flip()
                        else:
                           CMode = True
                           CaMode()
                           pygame.display.flip()#keyboard control
                    if event.key==ord('v'):
                        if Music == True:
                            pygame.mixer.music.pause()
                            Music = False
                        elif Music == False:
                            pygame.mixer.music.unpause()
                            Music = True
                if ChangeDirection=='right' and not Direction=='left' and Busy==False:
                    Direction=ChangeDirection
                    Busy = True
                if ChangeDirection=='left' and not Direction=='right' and Busy==False:
                    Direction=ChangeDirection
                    Busy = True
                if ChangeDirection=='up' and not Direction=='down' and Busy==False:
                    Direction=ChangeDirection
                    Busy = True
                if ChangeDirection=='down' and not Direction=='up' and Busy==False:
                    Direction=ChangeDirection
                    Busy = True#check the direction

            if Direction=='right':
                HeadPosition[0]+=20
            if Direction=='left':
                HeadPosition[0]-=20
            if Direction=='up':
                HeadPosition[1]-=20
            if Direction=='down':
                HeadPosition[1]+=20#change direction

            Busy = False

            SegmentsPosition.insert(0,list(HeadPosition))
            if HeadPosition[0]==FoodPosition[0] and HeadPosition[1]==FoodPosition[1]:
                FoodSpawned=0
                Sound()
            else:
                SegmentsPosition.pop()#python eat

            if FoodSpawned==0:
                x=random.randrange(1,32)
                y=random.randrange(1,32)
                FoodPosition=[int(x*20),int(y*20)]
            FoodSpawned=1#food spawn

            #surface.fill(ColorBlack)
            ColorRainbow = pygame.Color(random.randrange(50,255), random.randrange(50,255), random.randrange(50,255))

            pygame.draw.rect(surface,ColorBlack,Rect(0,0,640,640))
            surface.blit(Bimage, (0,0))

            for position in SegmentsPosition:
                pygame.draw.rect(surface,ColorWhite,Rect(position[0],position[1],20,20))
                pygame.draw.rect(surface,ColorRainbow,Rect(HeadPosition[0],HeadPosition[1],20,20))
            pygame.draw.rect(surface,ColorRed,Rect(FoodPosition[0],FoodPosition[1],20,20))
            #draw the snake on the screen

            if HeadPosition[0]>620 or HeadPosition[0]<0:
                GameOver()
            if HeadPosition[1]>620 or HeadPosition[1]<0:
                GameOver()
            for BodyPosition in SegmentsPosition[1:]:
                if HeadPosition[0]==BodyPosition[0] and HeadPosition[1]==BodyPosition[1]:
                    GameOver()
            global Score
            Score = 10 * len(SegmentsPosition) - 30
            pygame.draw.rect(surface,ColorGrey,Rect(640,0,360,640))
            surface.blit(SideLabel, (640, 0))
            ScoreFont=pygame.font.Font('freesansbold.ttf',32)
            ScoreSurf=ScoreFont.render('Score'+" "+str(10*len(SegmentsPosition)-30),True,ColorBlack)
            ScoreRect=ScoreSurf.get_rect()
            ScoreRect.topleft = (645, 10)
            global HighScore
            HighScoreFunc()
            ScoreSurf2 = ScoreFont.render('HighScore' + " " + str(HighScore), True, ColorBlack)
            ScoreRect2 = ScoreSurf2.get_rect()
            ScoreRect2.topleft = (645, 70)
            surface.blit(ScoreSurf,ScoreRect)
            surface.blit(ScoreSurf2, ScoreRect2)

            CaMode()

            pygame.display.flip()

            Challenge()

            fps.tick(fpsset)
startgame()
