import pygame,sys,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
#Constants
mousePosition = None
mousePressed = False
window_size = 800
obstacle_width = 80
path_width = 100

#Decide for player
def move_decide_self(object,list):
    print('Deciding!',object.x,object.y,list)
    if list[0] and object.x < 20 :
        move_up(object)
        print('1')
        return None
    if list[0] and window_size // 2 >= object.x >= 20 and object.y - object.speed > window_size//2 + obstacle_width // 2 :
        move_upleft(object)
        print('2')
        return None
    if list[0] and window_size // 2 >= object.x >= 20 and object.y - object.speed <= window_size//2 + obstacle_width // 2:
        move_left(object)
        print('3')
        return None
    if list[2] and object.x > window_size - path_width :
        move_up(object)
        print('4')
        return None
    if list[2] and 400 < object.x <= 750 and object.y - object.speed > window_size//2 + obstacle_width // 2:
        move_upright(object)
        print('5')
        return None
    if list[0] and window_size // 2 < object.x <= window_size - path_width and object.y - object.speed <= window_size//2 + obstacle_width // 2:
        move_right(object)
        print('6')
        return None

#Decide for AI
def move_decide_ai(object,list):
    '''Doc for move_decide_ai'''
    print('Deciding!', object.x, object.y, list)
    if list[0] and object.x < 20 :
        move_down(object)
        print('1')
        return None
    if list[0] and window_size // 2 >= object.x >= 20 and object.y + object.speed + object.size < window_size//2 - obstacle_width // 2 :
        move_downleft(object)
        print('2')
        return None
    if list[0] and window_size // 2 >= object.x >= 20 and object.y + object.speed <= window_size//2 - obstacle_width // 2:
        move_left(object)
        print('3')
        return None
    if list[2] and object.x > window_size - path_width:
        move_down(object)
        print('4')
        return None
    if list[2] and window_size // 2 < object.x <= window_size - path_width and object.y + object.speed + object.size < window_size//2 - obstacle_width // 2:
        move_downright(object)
        print('5')
        return None
    if list[0] and window_size // 2 < object.x <= window_size - path_width and object.y + object.speed <= window_size//2 - obstacle_width // 2:
        move_right(object)
        print('6')
        return None

#Move Functions

def move_up(object):
    object.y -= object.speed

def move_down(object):
    object.y += object.speed

def move_left(object):
    object.x -= object.speed

def move_right(object):
    object.x += object.speed

def move_upright(object):
    object.x += object.speed//2
    object.y -= object.speed//2

def move_downright(object):
    object.x += object.speed//2
    object.y += object.speed//2

def move_upleft(object):
    object.x -= object.speed//2
    object.y -= object.speed//2

def move_downleft(object):
    object.x -= object.speed//2
    object.y += object.speed//2

# Misc Functions

def quitGame():
    pygame.quit()
    sys.exit()

def check_events():
    global GAME_EVENTS,leftDown,rightDown,gameStarted
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftDown = True
            if event.key == pygame.K_RIGHT:
                rightDown = True
            if event.key == pygame.K_ESCAPE:
                quitGame()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftDown = False
            if event.key == pygame.K_RIGHT:
                rightDown = False
            if event.type == GAME_GLOBALS.QUIT:
                quitGame()