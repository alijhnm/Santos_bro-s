import pygame,sys,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import Classes,Constants

#Decide for player

def move_decide_self(object,enemy_building_list):
    '''Doc for move_decide_self'''
    if not enemy_building_list[0] and enemy_building_list[1] and object.y < 110 and object.x <= Constants.window_height//2:
        print('7')
        move_right(object)
        return None
    if not enemy_building_list[2] and enemy_building_list[1] and object.y < 110 and object.x > Constants.window_height//2:
        print('8')
        move_left(object)
        return None
    if (enemy_building_list[0] or (not enemy_building_list[0] and enemy_building_list[1]))  and object.x + object.size < Constants.path_width and object.y > 100:
        print('1')
        move_up(object)
        return None
    if (enemy_building_list[0] or (not enemy_building_list[0] and enemy_building_list[1])) and Constants.window_height // 2 >= object.x >= 0 and object.y - object.speed // 2 > Constants.window_height//2 + Constants.obstacle_width // 2 :
        print('2')
        move_upleft(object)
        return None
    if (enemy_building_list[0] or (not enemy_building_list[0] and enemy_building_list[1])) and Constants.window_height // 2 >= object.x  >= Constants.path_width - object.size and object.y - object.speed <= Constants. window_height // 2 + Constants.obstacle_width // 2:
        print('3')
        move_left(object)
        return None
    if (enemy_building_list[2] or (not enemy_building_list[2] and enemy_building_list[1])) and object.x > Constants.window_height - Constants.path_width and object.y > 100:
        print('4')
        move_up(object)
        return None
    if (enemy_building_list[2] or (not enemy_building_list[2] and enemy_building_list[1])) and Constants.window_height // 2  < object.x + object.size // 2 <= Constants.window_height - object.size // 2 and object.y - object.speed // 2 > Constants.window_height//2 + Constants.obstacle_width // 2:
        print('5')
        move_upright(object)
        return None
    if (enemy_building_list[2] or (not enemy_building_list[2] and enemy_building_list[1])) and Constants.window_height // 2 < object.x <= Constants.window_height - Constants.path_width and object.y - object.speed <= Constants.window_height//2 + Constants.obstacle_width // 2:
        print('6')
        move_right(object)
        return None

#Decide for AI

def move_decide_ai(object,player_building_list):
    '''Doc for move_decide_ai'''
    if not player_building_list[0] and player_building_list[1] and object.y > 690 and object.x <= Constants.window_height//2:
        move_right(object)
        return None
    if not player_building_list[2] and player_building_list[1] and object.y > 690 and object.x > Constants.window_height//2:
        move_left(object)
        return None
    if (player_building_list[0] or (not player_building_list[0] and player_building_list[1])) and object.x  < Constants.path_width - object.size :
        move_down(object)
        return None
    if (player_building_list[0] or (not player_building_list[0] and player_building_list[1])) and Constants.window_height // 2 >= object.x >= 20 and object.y + object.speed // 2 + object.size < Constants.window_height // 2 - Constants.obstacle_width // 2 :
        move_downleft(object)
        return None
    if (player_building_list[0] or (not player_building_list[0] and player_building_list[1])) and Constants.window_height // 2 >= object.x >= Constants.path_width - object.size and object.y + object.speed <= Constants.window_height//2 - Constants.obstacle_width // 2:
        move_left(object)
        return None
    if (player_building_list[2] or (not player_building_list[2] and player_building_list[1])) and object.x > Constants.window_height - Constants.path_width:
        move_down(object)
        return None
    if (player_building_list[2] or (not player_building_list[2] and player_building_list[1])) and Constants.window_height // 2 < object.x <= Constants.window_height - Constants.path_width and object.y + object.speed // 2 + object.size < Constants.window_height//2 - Constants.obstacle_width // 2:
        move_downright(object)
        return None
    if (player_building_list[2] or (not player_building_list[2] and player_building_list[1])) and Constants.window_height // 2 < object.x <= Constants.window_height - Constants.path_width and object.y + object.speed <= Constants.window_height//2 - Constants.obstacle_width // 2:
        move_right(object)
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
        if event.type == GAME_GLOBALS.QUIT:
            quitGame()

def make_troop(x,y,type,team_list):
    tmp = 'Classes.' + type + str((x,y))
    built_troop = eval(tmp)
    team_list.append(built_troop)

def check_attack(object,enemy_troop_list,enemy_building_list,window,time):
    '''Doc for check_attack'''
    if object.attack_range == 'Melee':
        attack_range = object.size
    else:
        attack_range = object.attack_range
    if object.target is not None:
        attack_target(object, window, enemy_troop_list,enemy_building_list, time)
    if object.target is None:
        for obj in enemy_troop_list:
            if type(obj) != bool:
                if (obj.x + obj.size//2 - object.x - object.size//2)**2 + (obj.y + obj.size//2 - object.y - object.size//2)**2 < attack_range ** 2 :
                    object.target = obj
    if object.target is None:
        for obj in enemy_building_list:
            if type(obj) != bool:
                if (obj.x + obj.size//2 - object.x - object.size//2)**2 + (obj.y + obj.size//2 - object.y - object.size//2)**2 < attack_range**2 :
                    object.target = obj

def attack_target(object,window,enemy_troop_list,enemy_building_list,time):
    if object.attack_range == 'Melee':
        attack_range = object.size
    else:
        attack_range = object.attack_range
    if (object.target.x + object.target.size//2 - object.x - object.size//2)**2 + (object.target.y + object.target.size//2 - object.y - object.size//2)**2 < attack_range ** 2:
        object.attack(time,window,enemy_troop_list,enemy_building_list)

def CheckBounds():
    global draggingCard,tmp_mouse
    if Constants.mousePressed == True:
        for card in Constants.Troop_list:
            if Constants.mousePosition[0] > card["position"][0] and Constants.mousePosition[0] < card["position"][0] + Constants.cardsSize:
                if Constants.mousePosition[1] > card["position"][1] and Constants.mousePosition[1] < card["position"][1] + Constants.cardsSize:
                   Constants.draggingCard[0] = True
                   Constants.draggingCard[1] = card["id"]
    if Constants.draggingCard[0] == True and Constants.mousePressed == False:
        Constants.tmp_mouse=(Constants.mousePosition[0],Constants.mousePosition[1])

def drawCard(window):
    tmp = [Constants.mousePosition[0],Constants.mousePosition[1]]
    for card in Constants.Troop_list:
        if tmp[1] < 400:
            tmp[1] = 400
        if tmp[0] > 700:
            tmp[0] = 700
        if Constants.draggingCard[0] == True and Constants.draggingCard[1] == card["id"]:
            window.blit(card["image"],(tmp[0] - Constants.cardsSize / 2,tmp[1] - Constants.cardsSize / 2))
            if Constants.draggingCard[0] == True:
                if pygame.mouse.get_pressed()[0]== False:
                    if Constants.elixir_costs[card['type']] <= Constants.elixir_count:
                        make_troop(tmp[0],tmp[1],card["type"],Constants.player_troop_list)
                        Constants.draggingCard[0] = False
                        Constants.elixir_count -= Constants.elixir_costs[card['type']]
    for card in Constants.cards:
        window.blit(card["image"],card["position"])

def Show_Menu(window,i):
    for card in Constants.all_Cards:
        window.blit(card["image"],card["position"])
    j = 0
    for card in Constants.Troop_list:
        window.blit(card['image'],Constants.tmp_mokhtasat[j])
        j += 1
    if pygame.mouse.get_pressed()[0] == 1:
        if len(Constants.Troop_list) < 4:
            for card in Constants.all_Cards:
                if Constants.mousePosition[0] > card["position"][0] and Constants.mousePosition[0] < card["position"][0] + Constants.cardsSize:
                    if Constants.mousePosition[1] > card["position"][1] and Constants.mousePosition[1] < card["position"][1] + Constants.cardsSize:
                        if Constants.all_Cards[card['id']] not in Constants.Troop_list:
                            window.blit(card["image"],Constants.tmp_mokhtasat[i])
                            print('Done')
                            i += 1
                            Constants.Troop_list.append(Constants.all_Cards[card["id"]])
        else:
            Constants.Game_Started = True
    for card in Constants.Troop_list:
        window.blit(card['image'],card['position'])






