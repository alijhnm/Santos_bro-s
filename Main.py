import pygame,sys,time,random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import Functions,Classes,Constants
window = pygame.display.set_mode((Constants.window_width,Constants.window_height))
#Functions.make_troop(100,300,'Barbarian',Constants.AI_troop_list)
#Functions.make_troop(100,250,'Barbarian',Constants.AI_troop_list)
#Functions.make_troop(500,150,'Barbarian',Constants.AI_troop_list)
#Functions.make_troop(200,200,'Barbarian',Constants.AI_troop_list)
#Functions.make_troop(300,300,'Barbarian',Constants.AI_troop_list)
queentower_left_enemy = Classes.Building(50,50,3000,100,200,1000,0,'king1.png',(255,0,0))
queentower_right_enemy = Classes.Building(650,50,3000,100,200,1000,0,'king1.png',(255,0,0))
kingtower_enemy = Classes.Building(350,50,3000,100,200,1000,0,'king1.png',(255,0,0))
kingtower_player = Classes.Building(350,650,3000,100,200,1000,0,'king1.png',(0,0,255))
queentower_left_player = Classes.Building(50,650,3000,100,200,1000,0,'king1.png',(0,0,255))
queentower_right_player = Classes.Building(650,650,3000,100,200,1000,0,'king1.png',(0,0,255))
Constants.player_building_list.append(queentower_left_player)
Constants.player_building_list.append(kingtower_player)
Constants.player_building_list.append(queentower_right_player)
Constants.AI_building_list.append(queentower_left_enemy)
Constants.AI_building_list.append(kingtower_enemy)
Constants.AI_building_list.append(queentower_right_enemy)
print(Constants.player_troop_list)
while True:
    Functions.check_events()
    Constants.mousePosition = pygame.mouse.get_pos()
    window.fill((0, 0, 0))
    if Constants.Game_Started == False and Constants.Game_Ended == False:
        Functions.Show_Menu(window,Constants.i)
    if Constants.Game_Started == True:
        window.fill((0, 0, 0))
        if GAME_TIME.get_ticks() - Constants.last_elixir > 3000 and Constants.elixir_count < 10:
            Constants.elixir_count += 1
            Constants.last_elixir = GAME_TIME.get_ticks()
        if Constants.elixir_count == 10:
            Constants.last_elixir = GAME_TIME.get_ticks()
        Functions.check_events()
        Constants.mousePosition = pygame.mouse.get_pos()
        for i in range(Constants.elixir_count):
            pygame.draw.rect(window,(255,0,255),(800,260 - 25 * i,120,20))
        if pygame.mouse.get_pressed()[0] == True:
            Constants.mousePressed = True
        else:
            Constants.mousePressed = False
        Functions.CheckBounds()
        Functions.drawCard(window)
        for self_troop in Constants.player_troop_list:
            if type(self_troop) != bool:
                Functions.check_attack(self_troop,Constants.AI_troop_list,Constants.AI_building_list,window,GAME_TIME.get_ticks())
                if self_troop.target is None:
                    Functions.move_decide_self(self_troop,Constants.AI_building_list)
                    self_troop.show(window,'dmfnljgbknsfdjk')
                self_troop.show(window, 'dmfnljgbknsfdjk')
        for self_building in Constants.player_building_list:
            if type(self_building) != bool:
                Functions.check_attack(self_building,Constants.AI_troop_list,Constants.AI_building_list,window,GAME_TIME.get_ticks())
                self_building.show(window)
        for enemy_obj in Constants.AI_troop_list:
            if type(enemy_obj) != bool:
                Functions.check_attack(enemy_obj, Constants.player_troop_list,Constants.player_building_list,window,GAME_TIME.get_ticks())
                if enemy_obj.target is None:
                    Functions.move_decide_ai(enemy_obj,Constants.player_building_list)
                    enemy_obj.show(window,'qwqr')
                enemy_obj.show(window, 'qwqr')
        for AI_building in Constants.AI_building_list:
            if type(AI_building) != bool:
                Functions.check_attack(AI_building,Constants.player_troop_list,Constants.player_building_list,window,GAME_TIME.get_ticks())
                AI_building.show(window)
    time.sleep(0.02)
    pygame.display.update()