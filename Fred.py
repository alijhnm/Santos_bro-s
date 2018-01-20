import pygame,sys,random,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
updown = False
timer = 0
pygame.init()
class Game():
    obstacle_list = []
    def __init__(self,score,height,width):
        self.score = score
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width,height))
        self.obstacles = []
        self.gravity = 1
    def quit(self):
        pygame.quit()
        sys.exit()


class Bird():

    def  __init__(self,X,Y,Height,Width,Vy,color,initVy,Bars):
        self.x = X
        self.y = Y
        self.height = Height
        self.width = Width
        self.init_vy = initVy
        self.vy = Vy
        self.color = color
        self.jumping = None
        self.bars = Bars

    def move(self):
        if self.vy > 1:
            self.vy = self.vy * 0.9
        else:
            self.vy = 0
            self.jumping = False
        if 0 < self.y < game.height - self.height:
            self.y += game.gravity
            game.gravity *= 1.1
        elif self.y >= game.height - self.height:
            player_y = game.height - self.height
            gravity = 1
        self.y -= self.vy

    def collision(self,game):
        if game.window.get_at((int(self.x + self.width),int(self.y))) == (255,255,255,255) or game.window.get_at((int(self.x + self.width),int(self.y + self.height))) == (255,255,255,255):
            return True
        else:
            return False

    def show(self):
        pygame.draw.rect(game.window,self.color,(self.x,self.y,self.width,self.height))


class Obstacle:
    last_obs_time = 0
    def __init__(self,game,bird):
        self.x = game.width
        self.width = 20
        self.speed = 1
        self.gap_y = random.randint(0,game.height - 2 * bird.height - 1)
        self.color = (255,255,255)
        self.gap_length = 2 * bird.height

    def move(self):
        self.x -= self.speed
        if self.x < self.width:
            del self

    def show(self,game):
        pygame.draw.rect(game.window,self.color,(self.x,0,self.width,game.height))
        pygame.draw.rect(game.window,(0,0,0),(self.x,self.gap_y,self.width,self.gap_length))


def quitGame():
    pygame.quit()
    sys.exit()

def gen_obs(game,bird,timer):
    obs = Obstacle(game,bird)
    game.obstacle_list.append(obs)
    Obstacle.last_obs_time = timer

def check_events():
    global GAME_EVENTS,updown,gameStarted
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                updown = True
            if event.key == pygame.K_ESCAPE:
                quitGame()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                updown = False
        if event.type == GAME_GLOBALS.QUIT:
            quitGame()

game = Game(0,800,800)
bird = Bird(game.width//2,game.width//2,40,20,0,(0,0,255),0,game.obstacle_list)
gen_obs(game,bird,timer)
# Main loop
while True :
    game.window.fill((0,0,0))
    check_events()
    timer = GAME_TIME.get_ticks()
    if timer - Obstacle.last_obs_time > 5000:
        gen_obs(game,bird,timer)
    for obs in game.obstacle_list:
        if bird.collision(game):
            print(game.obstacle_list[0])
            print('dead')
            quitGame()
    print((game.obstacle_list[-1].x+1,game.obstacle_list[-1].gap_y-1))
    print(game.window.get_at((game.obstacle_list[-1].x-1,game.obstacle_list[-1].gap_y-1)))
    if updown:
        bird.jumping = True
    bird.show()
    bird.move()
    for obs in game.obstacle_list:
        obs.show(game)
        obs.move()
    time.sleep(0.02)
    pygame.display.update()
