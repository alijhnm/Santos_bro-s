import pygame,sys,time,random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import Functions,Classes,Constants
window = pygame.display.set_mode((Constants.windowWidth,Constants.windowHeight))
Functions.make_troop(100,600,'Barbarian',Constants.player_troop_list)
Functions.make_troop(300,300,'Barbarian',Constants.AI_troop_list)
king_tower_enemy = Classes.Building(50,50,3000,100,200,1,0,'king1.png')
king_tower_player = Classes.Building(50,650,3000,100,200,1,0,'king1.png')
Constants.player_building_list.append(king_tower_player)
Constants.AI_building_list.append(king_tower_enemy)
while True:
    Functions.check_events()
    Constants.mousePosition = pygame.mouse.get_pos()
    window.fill((0,0,0))
    if pygame.mouse.get_pressed()[0] == True:
        Constants.mousePressed = True
    else:
        Constants.mousePressed = False
    Functions.CheckBounds()
    Functions.drawCard(window)
    pygame.draw.rect(window,(255,255,255),(Constants.path_width,Constants.windowHeight//2 - Constants.obstacle_width//2,Constants.window_size - 2 * Constants.path_width,Constants.obstacle_width))
    for self_troop in Constants.player_troop_list:
        Functions.check_attack(self_troop,Constants.AI_troop_list,Constants.AI_building_list,window,GAME_TIME.get_ticks())
        if self_troop.target is None:
            Functions.move_decide_self(self_troop)
            self_troop.show(window,'dmfnljgbknsfdjk')
        self_troop.show(window, 'dmfnljgbknsfdjk')
    for self_building in Constants.player_building_list:
        Functions.check_attack(self_building,Constants.AI_troop_list,Constants.AI_building_list,window,GAME_TIME.get_ticks())
        self_building.show(window)
    for enemy_obj in Constants.AI_troop_list:
        Functions.check_attack(enemy_obj, Constants.player_troop_list,Constants.player_building_list,window,GAME_TIME.get_ticks())
        if enemy_obj.target is None:
            Functions.move_decide_ai(enemy_obj)
            enemy_obj.show(window,'qwqr')
        enemy_obj.show(window, 'qwqr')
    for AI_building in Constants.AI_building_list:
        Functions.check_attack(AI_building,Constants.player_troop_list,Constants.player_building_list,window,GAME_TIME.get_ticks())
        AI_building.show(window)
    time.sleep(0.02)
    pygame.display.update()