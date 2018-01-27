import pygame,sys,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import Classes,Constants

#Decide for player

def move_decide_self(object):
    '''Doc for move_decide_self'''
    if object.x + object.size < Constants.path_width :
        move_up(object)
        return None
    if Constants.windowHeight // 2 >= object.x >= 0 and object.y - object.speed // 2 > Constants.windowHeight//2 + Constants.obstacle_width // 2 :
        move_upleft(object)
        return None
    if Constants.windowHeight // 2 >= object.x  >= Constants.path_width - object.size and object.y - object.speed <= Constants. windowHeight // 2 + Constants.obstacle_width // 2:
        move_left(object)
        return None
    if object.x > Constants.window_size - Constants.path_width :
        move_up(object)
        return None
    if Constants.windowHeight // 2  < object.x + object.size // 2 <= Constants.windowHeight - object.size // 2 and object.y - object.speed // 2 > Constants.windowHeight//2 + Constants.obstacle_width // 2:
        move_upright(object)
        return None
    if Constants.windowHeight // 2 < object.x <= Constants.windowHeight - Constants.path_width and object.y - object.speed <= Constants.windowHeight//2 + Constants.obstacle_width // 2:
        move_right(object)
        return None

#Decide for AI

def move_decide_ai(object):
    '''Doc for move_decide_ai'''
    if object.x  < Constants.path_width - object.size :
        move_down(object)
        return None
    if Constants.windowHeight // 2 >= object.x >= 20 and object.y + object.speed // 2 + object.size < Constants.windowHeight // 2 - Constants.obstacle_width // 2 :
        move_downleft(object)
        return None
    if Constants.windowHeight // 2 >= object.x >= Constants.path_width - object.size and object.y + object.speed <= Constants.windowHeight//2 - Constants.obstacle_width // 2:
        move_left(object)
        return None
    if object.x > Constants.window_size - Constants.path_width:
        move_down(object)
        return None
    if Constants.windowHeight // 2 < object.x <= Constants.windowHeight - Constants.path_width and object.y + object.speed // 2 + object.size < Constants.windowHeight//2 - Constants.obstacle_width // 2:
        move_downright(object)
        return None
    if Constants.windowHeight // 2 < object.x <= Constants.windowHeight - Constants.path_width and object.y + object.speed <= Constants.windowHeight//2 - Constants.obstacle_width // 2:
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
    for obj in enemy_troop_list:
        if object.target is not None:
            attack_target(object,window,enemy_troop_list,time)
        elif (obj.x + obj.size - object.x - object.size)**2 + (obj.y + obj.size - object.y - object.size)**2 < attack_range ** 2 :
            object.target = obj
    if object.target is None:
        for obj in enemy_building_list:
            if (obj.x + obj.size - object.x - object.size)**2 + (obj.y + obj.size - object.y - object.size)**2 < attack_range**2 :
                object.target(obj)

def attack_target(object,window,enemy_team,time):
    if object.attack_range == 'Melee':
        attack_range = object.size
    else:
        attack_range = object.attack_range
    if (object.target.x + object.target.size - object.x - object.size)**2 + (object.target.y + object.target.size - object.y - object.size)**2 < attack_range ** 2:
        object.attack(time,window,enemy_team)

def CheckBounds():
    global cards,draggingCard,tmp_mouse

    if Constants.mousePressed == True:
        #is our cursor over the square?
        for card in cards:
                if Constants.mousePosition[0] > card["position"][0] and Constants.mousePosition[0] < card["position"][0] + Constants.cardsSize:

                    if Constants.mousePosition[1] > card["position"][1] and Constants.mousePosition[1] < card["position"][1] + Constants.cardsSize:

                        draggingCard[0] = True
                        draggingCard[1] = card["id"]

    if draggingCard[0] == True and Constants.mousePressed == False:
        draggingCard[0] = False
        tmp_mouse=(Constants.mousePosition[0],Constants.mousePosition[1])
    print(tmp_mouse)


def drawCard(window):
    global cards,draggingCard
    tmp = [Constants.mousePosition[0],Constants.mousePosition[1]]
    for card in cards:
        if tmp[1] < 400:
            tmp[1] = 400
        #if card["id"] == i:
        if draggingCard[0] == True and draggingCard[1] == card["id"]:
            window.blit(card["image"],(tmp[0] - Constants.cardsSize / 2,tmp[1] - Constants.cardsSize / 2))

    for card in cards:
        window.blit(card["image"],card["position"])
