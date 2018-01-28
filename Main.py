import pygame,sys,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import Functions,Classes,Constants

#Making the games window

window = pygame.display.set_mode((Constants.window_width,Constants.window_height))

#Making buildings of the game

queentower_left_enemy = Classes.Building(50,50,3000,100,200,500,0,'QueenTower_AI.png',(255,0,0))
queentower_right_enemy = Classes.Building(650,50,3000,100,200,500,0,'QueenTower_AI.png',(255,0,0))
kingtower_AI = Classes.Building(350,50,3000,100,200,1000,0,'KingTower_AI.png',(255,0,0))
kingtower_player = Classes.Building(350,650,3000,100,200,1000,0,'KingTower.png',(0,0,255))
queentower_left_player = Classes.Building(50,650,3000,100,200,500,0,'QueenTower.png',(0,0,255))
queentower_right_player = Classes.Building(650,650,3000,100,200,500,0,'QueenTower.png',(0,0,255))

Constants.player_building_list.append(queentower_left_player)
Constants.player_building_list.append(kingtower_player)
Constants.player_building_list.append(queentower_right_player)
Constants.AI_building_list.append(queentower_left_enemy)
Constants.AI_building_list.append(kingtower_AI)
Constants.AI_building_list.append(queentower_right_enemy)

#Main loop

while True:
    Functions.check_events()
    Constants.mousePosition = pygame.mouse.get_pos()
    if len(Constants.game_cards) >= 4:
        Constants.game_started = True
        for card_number in range(len(Constants.game_cards)):
            Constants.game_cards[card_number]['position'] = Constants.game_coordinates[card_number]
    if Constants.game_started == True and Constants.game_finished == True:
        if not Constants.AI_building_list[1]:
            window.blit(Constants.win_image,(0,0))
        else:
            window.blit(Constants.lose_image,(0,0))
    if (not Constants.game_started) and (not Constants.game_finished):
        Functions.Show_menu(window,Constants.i,Constants.game_started)
    if Constants.game_started == True and Constants.game_finished == False:
        if Functions.check_result(Constants.player_building_list,Constants.AI_building_list):
            Constants.game_finished = True
        else:
            if Constants.game_paused:
                Functions.pause_game(window)
            else:
                window.fill((0, 0, 0))
                window.blit(Constants.map,(0,0))
                if GAME_TIME.get_ticks() - Constants.last_elixir_player > Constants.elixir_interval and Constants.elixir_count_player < 10:
                    Constants.elixir_count_player += 1
                    Constants.last_elixir_player = GAME_TIME.get_ticks()
                if Constants.elixir_count_player == 10:
                    Constants.last_elixir = GAME_TIME.get_ticks()
                Constants.mousePosition = pygame.mouse.get_pos()
                for i in range(Constants.elixir_count_player):
                    pygame.draw.rect(window,(255,0,255),(800,260 - 25 * i,120,20))
                if pygame.mouse.get_pressed()[0] == True:
                    Constants.mousePressed = True
                else:
                    Constants.mousePressed = False
                Functions.CheckBounds()
                Functions.drawCard(window)
                for self_building in Constants.player_building_list:
                    if type(self_building) != bool:
                        Functions.check_attack(self_building,Constants.AI_troop_list,Constants.AI_building_list,window,GAME_TIME.get_ticks())
                        self_building.show(window)
                for enemy_obj in Constants.AI_troop_list:
                    if type(enemy_obj) != bool:
                        Functions.check_attack(enemy_obj, Constants.player_troop_list,Constants.player_building_list,window,GAME_TIME.get_ticks())
                        if enemy_obj.target is None:
                            Functions.move_decide_ai(enemy_obj,Constants.player_building_list)
                            enemy_obj.show(window,'move_down_image')
                        enemy_obj.show(window, 'move_down_image')
                for AI_building in Constants.AI_building_list:
                    if type(AI_building) != bool:
                        Functions.check_attack(AI_building,Constants.player_troop_list,Constants.player_building_list,window,GAME_TIME.get_ticks())
                        AI_building.show(window)
                for self_troop in Constants.player_troop_list:
                    if type(self_troop) != bool:
                        Functions.check_attack(self_troop,Constants.AI_troop_list,Constants.AI_building_list,window,GAME_TIME.get_ticks())
                        if self_troop.target is None:
                            Functions.move_decide_self(self_troop,Constants.AI_building_list)
                            self_troop.show(window,'move_up_image')
                        self_troop.show(window, 'move_up_image')
                time.sleep(0.05)
    pygame.display.update()