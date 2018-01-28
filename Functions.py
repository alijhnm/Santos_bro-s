import pygame,sys,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import Classes,Constants

#Decide for player
def move_decide_self(object,enemy_building_list):
    '''This function makes desicion for movement of a card in player team based on its current position in the game and the enemy team buildings.\
    Takes an object of player team and the entire enemy building list as input arguments and changes the position of the object.\
    The None returned after each change in position is essential for preventing one object from making multiple desicions in one turn.'''
    if not enemy_building_list[0] and enemy_building_list[1] and object.y < 110 and object.x <= Constants.window_height//2:
        move_right(object)
        return None
    if not enemy_building_list[2] and enemy_building_list[1] and object.y < 110 and object.x > Constants.window_height//2:
        move_left(object)
        return None
    if (enemy_building_list[0] or (not enemy_building_list[0] and enemy_building_list[1]))  and object.x + object.size < Constants.path_width and object.y > 100:
        move_up(object)
        return None
    if (enemy_building_list[0] or (not enemy_building_list[0] and enemy_building_list[1])) and Constants.window_height // 2 >= object.x >= 0 and object.y - object.speed // 2 > Constants.window_height//2 + Constants.obstacle_width // 2 :
        move_upleft(object)
        return None
    if (enemy_building_list[0] or (not enemy_building_list[0] and enemy_building_list[1])) and Constants.window_height // 2 >= object.x  >= Constants.path_width - object.size and object.y - object.speed <= Constants. window_height // 2 + Constants.obstacle_width // 2:
        move_left(object)
        return None
    if (enemy_building_list[2] or (not enemy_building_list[2] and enemy_building_list[1])) and object.x > Constants.window_height - Constants.path_width and object.y > 100:
        move_up(object)
        return None
    if (enemy_building_list[2] or (not enemy_building_list[2] and enemy_building_list[1])) and Constants.window_height // 2  < object.x + object.size // 2 <= Constants.window_height - object.size // 2 and object.y - object.speed // 2 > Constants.window_height//2 + Constants.obstacle_width // 2:
        move_upright(object)
        return None
    if (enemy_building_list[2] or (not enemy_building_list[2] and enemy_building_list[1])) and Constants.window_height // 2 < object.x <= Constants.window_height - Constants.path_width and object.y - object.speed <= Constants.window_height//2 + Constants.obstacle_width // 2:
        move_right(object)
        return None

#Decide for AI

def move_decide_ai(object,player_building_list):
    '''Works just like the move_decide_player but because of difference in placement of teams has different if statements'''
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
#For better abstraction we have implemented this simple move functions so that reading the code becomes easy
#This functions simply do what their name is.They modify an objects x and y so that is shown in a different position next frame
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
    '''Quits the game properly'''
    pygame.quit()
    sys.exit()

def check_events():
    '''This function is used to get the events that are passed into compuyer by consumer.It is always called at the start of the mainloop.\
    It needs no input arguments because we dont need to change anyrhing;Instead,we want to understand the changes by using pygame'''
    global GAME_EVENTS,leftDown,rightDown,gameStarted
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            quitGame()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if Constants.game_paused:
                    Constants.game_paused = False
                else:
                    Constants.game_paused = True

def make_troop(x,y,type,team_list):
    '''Takes a coordinate,a type and a list and makes a troop at given coordinate with given type and addes the troop to given\
    list,be it player or AI troop list'''
    if team_list == Constants.AI_troop_list:
        color = (255,0,0)
    else:
        color = (0,0,255)
    tmp = 'Classes.' + type + str((x,y,color))
    built_troop = eval(tmp)
    team_list.append(built_troop)

def check_attack(object,enemy_troop_list,enemy_building_list,window,time):
    '''Checks an objects target.If it has one,the object will attack the target.Otherwise,checks if their is any enemy\
    troop or building in the given objects attack range or not.If there is any,This function will set the objects target\
    to the enemy troop or building found.It also gets the games window and its time as input arguments because they are\
    needed for attack_target function to function correctly'''
    if object.attack_range == 'Melee': #If given objects attack range is melee,it means that it can attack another object right next to it
        attack_range = object.size
    else:
        attack_range = object.attack_range
    if object.target is not None: #If objects target gets out of its attack range its target attribute must be set to None
        if (object.target.x + object.target.size // 2 - object.x - object.size // 2) ** 2 + (
                object.target.y + object.target.size // 2 - object.y - object.size // 2) ** 2 > attack_range ** 2:
            object.target = None
    if object.target is not None:
        attack_target(object, window, enemy_troop_list,enemy_building_list, time)
    if object.target is None: #Check if any of enemy troops is in objects attack range
        for obj in enemy_troop_list:
            if type(obj) != bool:
                if (obj.x + obj.size//2 - object.x - object.size//2)**2 + (obj.y + obj.size//2 - object.y - object.size//2)**2 <= attack_range ** 2 :
                    if type(object) == Classes.Building:
                        object.target = obj
                    elif (object.target_type == 'Ground' and obj.type == 'Ground') or object.target_type == 'Air $ Ground': #or (type(object) != Classes.Ballon and type(object) != Classes.Giant and type(object) != Classes.Hog)
                        object.target = obj
    if object.target is None: #Check if any of enemy buildings is in objects attack range
        for obj in enemy_building_list:
            if type(obj) != bool:
                if (obj.x + obj.size//2 - object.x - object.size//2)**2 + (obj.y + obj.size//2 - object.y - object.size//2)**2 <= attack_range**2 :
                    object.target = obj

def attack_target(object,window,enemy_troop_list,enemy_building_list,time):
    '''Takes an object,games window,games time and enemy building and troop lists as input arguments and calls the attack method of object.'''
    if object.attack_range == 'Melee': #Same statement as the one in check_attack function
        attack_range = object.size
    else:
        attack_range = object.attack_range
    if (object.target.x + object.target.size//2 - object.x - object.size//2)**2 + (object.target.y + object.target.size//2 - object.y - object.size//2)**2 <= attack_range ** 2:
        object.attack(time,window,enemy_troop_list,enemy_building_list)

def CheckBounds():
    '''Checks the outer limits of cards shown at right of the game screen and if the mouse is pressed on them,\
    it will set that cards draggindcard parameter True'''
    global cards,draggingCard,tmp_mouse
    if Constants.mousePressed == True:
        for card in Constants.game_cards:
            if Constants.mousePosition[0] > card["position"][0] and Constants.mousePosition[0] < card["position"][0] + Constants.cardsSize:
                if Constants.mousePosition[1] > card["position"][1] and Constants.mousePosition[1] < card["position"][1] + Constants.cardsSize:
                   Constants.draggingCard[0] = True
                   Constants.draggingCard[1] = card["id"]
    if Constants.draggingCard[0] == True and Constants.mousePressed == False:
        Constants.tmp_mouse=(Constants.mousePosition[0],Constants.mousePosition[1])

def drawCard(window):
    '''Draws  cards that are at the right of the screen in the game and the card which is being dragged(if any) on the \
     surface of the game.if mouse is released it will call the make_troop function and make a troop at the position of \
     the dragging card.'''
    tmp = [Constants.mousePosition[0],Constants.mousePosition[1]]
    for card in Constants.game_cards:
        if tmp[1] < 400:
            tmp[1] = 400
        if tmp[0] > 700:
            tmp[0] = 700
        if Constants.draggingCard[0] == True and Constants.draggingCard[1] == card["id"]:
            window.blit(card["image"],(tmp[0] - Constants.cardsSize / 2,tmp[1] - Constants.cardsSize / 2))
            if Constants.draggingCard[0] == True:
                if pygame.mouse.get_pressed()[0]== False:
                    if Constants.elixir_costs[card['type']] <= Constants.elixir_count_player:
                        make_troop(tmp[0],tmp[1],card["type"],Constants.player_troop_list)
                        Constants.draggingCard[0] = False
                        Constants.elixir_count_player -= Constants.elixir_costs[card['type']]
    for card in Constants.game_cards:
        window.blit(card["image"],card["position"])

def Show_menu(window,i,game_started):
    '''Handles the first screen of the game which is menu screen and that is the screen that you choose your game cards.'''
    window.blit(Constants.menu_image,(0,0))
    for card in Constants.all_Cards:
        window.blit(card["image"],card["position"])
    number_of_selected_cards = 0
    for card in Constants.game_cards:
        window.blit(card['image'],Constants.menu_coordinates[number_of_selected_cards])
        number_of_selected_cards += 1
    if pygame.mouse.get_pressed()[0] == 1:
        for card in Constants.all_Cards:
            if Constants.mousePosition[0] > card["position"][0] and Constants.mousePosition[0] < card["position"][0] + Constants.cardsSize:
                if Constants.mousePosition[1] > card["position"][1] and Constants.mousePosition[1] < card["position"][1] + Constants.cardsSize:
                    if Constants.all_Cards[card['id']] not in Constants.game_cards:
                        window.blit(card["image"],Constants.menu_coordinates[i])
                        i += 1
                        Constants.game_cards.append(Constants.all_Cards[card["id"]])

def check_result(player_building_list,AI_building_list):
    '''Checks if the game is finished or not.Return the result of the game if it is finished(win or lose);False otherwise'''
    result = False
    if not player_building_list[1]:
        result = 'Lose'
    if not AI_building_list[1]:
        result = 'Win'
    return result

def pause_game(window):
    '''Pauses the game and enters a while loop which will terminate if escape button is pressed.The information of escape \
    button is updated with check_events function in each loop'''
    while Constants.game_paused:
        check_events()

def AI(player_list,ai_list,elixir_count,last_elixir):
    pass