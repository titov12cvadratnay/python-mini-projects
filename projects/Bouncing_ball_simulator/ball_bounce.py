#This program shows the simulation of 5 balls bouncing under gravitational acceleration.
#It is also accompanied by eleastic collission with walls of the container.
#It is fun to watch.
import pygame,time,random

pygame.init()

#setting screen size of pygame window to 800 by 600 pixels
screen=pygame.display.set_mode((800,600))
background=pygame.image.load(r"background-img.jpg")

# sound and text:)
hit_sound = pygame.mixer.Sound(r"3bae27a36ef885f.mp3")
font = pygame.font.SysFont('microsoftjhenghei', 36)  
text_surface = font.render("Ball Bounce Simulation", True, (255, 255, 255))  

#Adding title
pygame.display.set_caption('Ball Bounce Simulation')

class ball:
    ball_image=pygame.image.load(r"ball.png")
    g=1
    def __init__(self):
        self.velocityX=4
        self.velocityY=4
        self.X=random.randint(0,768)
        self.Y=random.randint(0,350)

    def render_ball(self):
        screen.blit(ball.ball_image, (self.X,self.Y))
    def move_ball(self):
        #changing y component of velocity due to downward acceleration
        self.velocityY+=ball.g
        #changing position based on velocity
        self.X+=self.velocityX
        self.Y+=self.velocityY
        #collission with the walls lead to change in velocity
        if self.X<0 or self.X>768:
            self.velocityX*=-1
            hit_sound.play()
        if self.Y<0 and self.velocityY<0:
            self.velocityY*=-1
            hit_sound.play()
            self.Y=0
        if self.Y>568 and self.velocityY>0:
            self.velocityY*=-1
            hit_sound.play()
            self.Y=568
#list of balls created as objects
Ball_List=[ball(),ball(), ball(), ball(), ball()]

#The main program loop
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:     #space detector
            Ball_List = [ball()]
            
    
    time.sleep(0.02)
    screen.blit(background, (0,0))
    screen.blit(text_surface, (200, 200))
    for ball_item in Ball_List:
        ball_item.render_ball()
        ball_item.move_ball()
    pygame.display.update()
