import pygame,sys,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import Functions,Classes
b = Classes.Barbarian(150,650)
a = Classes.Archer(200,100)
enemy_list = [True,True,True]
window = pygame.display.set_mode((800,800))
building = Classes.Building(0,0,2000,100,500,1000,500,'building.png')
while True:
    Functions.check_events()
    window.fill((0,0,0))
    pygame.draw.rect(window,(255,255,255),(100,360,600,80))
    Functions.move_decide_self(b,enemy_list)
    building.show(window)
    window.blit(b.image,(b.x,b.y))
    time.sleep(0.02)
    pygame.display.update()