import pygame
import ptext
from dialogtree import UIdialogbase
WIDTH, HEIGHT = 840, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
#screen = pygame.display.set_mode((WIDTH, HEIGHT))
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [3, 3]
paddle_pos = HEIGHT/2 - PADDLE_HEIGHT/2
game_over = False
class pongdia(UIdialogbase):
    def initialise(self):
        global ball_pos
        ball_pos = [WIDTH/2, HEIGHT/2]
        self.game_over = False
        self.initialised = 1
        self.score = 0
        self.add_btn("exit","exitbtn",(0.9,0.9),(0.1,0.1))
        self.add_btn("restart","re",(0.9,0.8),(0.1,0.1))
    def renderframe(self):
        global ball_pos
        paddle_pos[1] = pygame.mouse.get_pos()[1]
        self.active = self.gameover
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        if ball_pos[1] < BALL_RADIUS or ball_pos[1] > HEIGHT - BALL_RADIUS:
            ball_vel[1] = -ball_vel[1]
            self.score +=1
        if ball_pos[0] < PADDLE_WIDTH and paddle_pos - BALL_RADIUS < ball_pos[1] < paddle_pos + PADDLE_HEIGHT + BALL_RADIUS:
            ball_vel[0] = -ball_vel[0]
            self.score +=1
        if ball_pos[0] < 0:
        game_over = True

        screen.fill((0, 0, 0))
        pygame.draw.rect(self.drawsys.screen, (255, 255, 255), (WIDTH/2 - 1, 0, 2, HEIGHT))
        pygame.draw.circle(self.drawsys.screen, (255, 255, 255), ball_pos, BALL_RADIUS)
        pygame.draw.rect(self.drawsys.screen, (255, 255, 255), (0, paddle_pos, PADDLE_WIDTH, PADDLE_HEIGHT))
        ptext.draw("score ; " + str(self.score) ,pos=(20,20),color="white" )
    def btnp(self,name):
        global ball_pos
        if name == "exitbtn":
            self.active = 0
        if name == "re":
            self.score = 0
            self.active = 1
            ball_pos = [WIDTH/2, HEIGHT/2]
