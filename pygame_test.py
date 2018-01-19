import pygame,sys,random,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
pygame.init()
window_width = 800
window_height = 800
surface = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Pygame Mouse!')
mouse_position = None
mouse_pressed = False
player_size = 40
player_color = (255,255,255)
player_x = window_height / 2
player_y = window_height - player_size
dragging = False
gravity = 5
def check_bounds():
    global player_color,player_x,player_y,dragging
    if mouse_pressed :
        if player_x + player_size > mouse_position[0] > player_x:
            if player_y + player_size > mouse_position[1] > player_y:
                dragging = True
                pygame.mouse.set_visible(0)
    else :
        player_color = (255,0,0)
        pygame.mouse.set_visible(1)
        dragging = False
def check_gravity():
    global gravity,player_y,player_size,window_height
    if player_y < window_height - player_size and mouse_pressed == False:
        player_y += gravity
        gravity *= 1.1
    else:
        player_y = window_height - player_size
        gravity = 5
def draw_player():
    global  player_color,player_x,player_y,dragging
    if dragging:
        player_color = (0,255,0)
        player_x = mouse_position[0] - player_size / 2
        player_y = mouse_position[1] - player_size / 2
    pygame.draw.rect(surface,player_color,(player_x,player_y,player_size,player_size))
def quitgame():
    pygame.quit()
    sys.exit()
while True :
    mouse_position = pygame.mouse.get_pos()
    surface.fill((200,200,200))
    if pygame.mouse.get_pressed()[0]:
        mouse_pressed = True
    else :
        mouse_pressed = False
    check_bounds()
    check_gravity()
    draw_player()
    pygame.display.update()
    time.sleep(0.02)
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitgame()
        if event.type == GAME_GLOBALS.QUIT:
            quitgame()
            
