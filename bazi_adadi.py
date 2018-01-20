import pygame,sys,random,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
pygame.init()
window_width = 800
window_height = 800
surface = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Pygame Keyboard!')
player_size = 50
player_x = window_height / 2
player_y = window_width / 2
player_vx = 1.0
player_vy = 0.0
jump_height = 25
move_speed = 1
max_speed = 10
gravity = 1
leftdown = False
rightdown = False
jumped = False
def move():
    global player_x,player_y,player_vx,player_vy,jumped,gravity
    if leftdown :
        if player_vx > 0 :
            player_vx = -move_speed
        if player_x > 0 :
            player_x += player_vx
    if rightdown :
        if player_vx < 0 :
            player_vx = move_speed
        if player_x + player_size < window_width:
            player_x += player_vx
    if player_vy > 1:
        player_vy = player_vy * 0.9
    else:
        player_vy = 0
        jumped = False
    if 0 < player_y < window_height - player_size:
        player_y += gravity
        gravity *= 1.1
    elif player_y >= window_height - player_size:
        player_y = window_height - player_size
        gravity = 1
    elif player_y <= 0 :
        player_y = 1
    player_y -= player_vy
    if (player_vx > 0 and player_vx < max_speed) or\
            (player_vx < 0 and player_vx > -max_speed):
        if not jumped and (leftdown or rightdown):
            player_vx = player_vx * 1.1
def quitgame():
    pygame.quit()
    sys.exit()
while True :
    surface.fill((0,0,0))
    pygame.draw.rect(surface,(255,0,0),(player_x,player_y,player_size,player_size))
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                leftdown = True
            if event.key == pygame.K_RIGHT:
                rightdown = True
            if event.key == pygame.K_UP:
                jumped = True
                player_vy += jump_height
                gravity = 1
            if event.key == pygame.K_ESCAPE:
                quitgame()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftdown = False
                player_vx = move_speed
            if event.key == pygame.K_RIGHT:
                rightdown = False
                player_vx = move_speed
        if event.type == GAME_GLOBALS.QUIT:
            quitgame()
    move()
    time.sleep(0.02)
    pygame.display.update()