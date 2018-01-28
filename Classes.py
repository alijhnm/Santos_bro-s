import pygame,sys,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import Functions,Constants
pygame.init()

#General Card class

class Card:
    '''This is the main class of the game.All attributes of cards except the initial position and cards team color is \
    initialized here'''
    def __init__(self,MaxHealth,Speed,AttackDamage,Type,TargetType,AttackRange,AttackInterval,Size):
        self.x = None # X of troops cordinate.Initialy it is None but when an object of a subclass is made it is given as arguments
        self.y = None # Y of troops cordinate.
        self.max_health = MaxHealth #Maximum health of a troop used for drawing cards health bar
        self.hp = MaxHealth #When a troop is made its initial health is maximum health
        self.speed = Speed #Move speed of a troop
        self.attack_damage = AttackDamage
        self.type = Type #Type of troop(ground or air unit)
        self.target_type = TargetType
        self.attack_range = AttackRange
        self.attack_interval = AttackInterval #Delay between attacks
        self.size = Size
        self.elixir_cost = None
        self.target = None
        self.attack_image = None
        self.move_up_image = None
        self.move_down_image = None
        self.last_attack = 0 #Time of troops last attack
        self.team_color = None

    def show(self,window,image):
        '''Show a troop in its position on the game window.Based on the team that the troop is in in must be shown with \
        a differet image'''
        shown_image = 'self.' + image
        window.blit(eval(shown_image),(self.x,self.y))
        pygame.draw.rect(window,(100,100,100),(self.x,self.y - Constants.hp_bar_offset,self.size,Constants.hp_bar_width))
        pygame.draw.rect(window,self.team_color,(self.x,self.y - Constants.hp_bar_offset,int(self.hp / self.max_health * self.size),Constants.hp_bar_width))

    def attack(self,time,window,enemy_troop_list,enemy_building_list):
        '''Attacks a troops target;That is,decreesing targets hp by troops attack damage units.If the target is dead,\
        This function will properly remove the the target from the game.Also changes the time of a troops last attack'''
        if time - self.last_attack > self.attack_interval:
            self.target.hp -= self.attack_damage
            self.last_attack = time
            window.blit(self.move_up_image,(self.x,self.y))
            pygame.draw.line(window,(255,0,0),(self.x + self.size//2,self.y + self.size//2),(self.target.x + self.target.size//2,self.target.y + self.target.size//2))
            if self.target.hp <= 0:
                if self.target in enemy_troop_list:
                    enemy_troop_list[enemy_troop_list.index(self.target)] = False
                if self.target in enemy_building_list:
                    enemy_building_list[enemy_building_list.index(self.target)] = False
                self.target = None
        else:
            window.blit(self.move_up_image,(self.x,self.y))


class Barbarian(Card):
    '''Sweet awsome allrounder!'''
    def __init__(self,X,Y,TeamColor):
        Card.__init__(self,636,Constants.medium_speed,159,'Ground','Ground','Melee',1500,False,Constants.medium_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 2
        self.move_up_image = pygame.image.load('Barbarian-move_up.png')
        self.move_down_image = pygame.image.load('Barbarian-move_down.png')
        self.team_color = TeamColor


class Archer(Card):

    def __init__(self,X,Y,TeamColor):
        Card.__init__(self,254,Constants.medium_speed,86,'Ground','Air $ Ground',5 * Constants.AttackRange,1200,False,Constants.small_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 2
        self.move_up_image = pygame.image.load('Archer-move_up.png')
        self.move_down_image = pygame.image.load('Archer-move_down.png')
        self.team_color = TeamColor


class Giant(Card):

    def __init__(self, X, Y,TeamColor):
        Card.__init__(self, 3344, Constants.low_speed, 211, 'Ground', 'Building', 'Melee', 1500,
                      'False', Constants.big_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 5
        self.move_up_image = pygame.image.load('Giant-move_up.png')
        self.move_down_image = pygame.image.load('Giant-move_down.png')
        self.team_color = TeamColor


class Dragon(Card):

    def __init__(self, X, Y,TeamColor):
        Card.__init__(self, 1064, Constants.fast_speed, 133, 'Air', 'Air $ Ground', 3.5 * Constants.AttackRange, 1600, Constants.small_area_of_effect, Constants.medium_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 4
        self.move_up_image = pygame.image.load('Dragon-move_up.png')
        self.move_down_image = pygame.image.load('Dragon-move_down.png')
        self.team_color = TeamColor



class PEKKA(Card):

    def __init__(self, X, Y,TeamColor):
        Card.__init__(self, 3458, Constants.low_speed, 678, 'Ground', 'Ground', 'Melee', 2000,False, Constants.big_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 7
        self.move_up_image = pygame.image.load('PEKKA-move_up.png')
        self.move_down_image = pygame.image.load('PEKKA-move_down.png')
        self.team_color = TeamColor


class Ballon(Card):

    def __init__(self, X, Y,TeamColor):
        Card.__init__(self, 798, Constants.medium_speed, 798, 'Air', 'Building', 'Melee', 3000,Constants.medium_area_of_effect, Constants.big_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 5
        self.move_up_image = pygame.image.load('Ballon.png')
        self.move_down_image = pygame.image.load('Ballon.png')
        self.team_color = TeamColor


class Hog(Card):

    def __init__(self, X, Y,TeamColor):
        Card.__init__(self, 1000, Constants.fast_speed, 160, 'Ground', 'Building', 'Melee', 1200,False, Constants.medium_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 4
        self.move_up_image = pygame.image.load('Hog-move_up.png')
        self.move_down_image = pygame.image.load('Hog-move_down.png')
        self.team_color = TeamColor


class Building:
    '''General building class.'''
    def __init__(self,X,Y,MaxHealth,AttackDamage,AttackRange,AttackInterval,AreaOfEffect,Address,TeamColor):
        self.x = X
        self.y = Y
        self.max_health = MaxHealth
        self.hp = MaxHealth
        self.current_health = MaxHealth
        self.attack_damage = AttackDamage
        self.attack_range = AttackRange
        self.attack_interval = AttackInterval
        self.area_of_effect = AreaOfEffect
        self.image = pygame.image.load(Address)
        self.target = None
        self.size = 100
        self.last_hit = 0
        self.team_color = TeamColor

    def show(self,window):
        ''''Shows a building at its current location in the game'''
        window.blit(self.image,(self.x,self.y))
        pygame.draw.rect(window, (100, 100, 100),(self.x, self.y - Constants.hp_bar_offset, self.size, Constants.hp_bar_width))
        pygame.draw.rect(window, self.team_color,(self.x, self.y - Constants.hp_bar_offset, int(self.hp / self.max_health * self.size), Constants.hp_bar_width))

    def attack(self,time,window,enemy_troop_list,enemy_building_list):
        '''Works like the attack method for troops'''
        if time - self.last_hit > self.attack_interval:
            self.target.hp -= self.attack_damage
            self.last_hit = time
            pygame.draw.line(window, (255, 255, 255), (self.x + self.size//2, self.y + self.size//2),(self.target.x + self.target.size//2, self.target.y + self.target.size//2))
        if self.target.hp <= 0:
            if self.target in enemy_troop_list:
                enemy_troop_list[enemy_troop_list.index(self.target)] = False
            if self.target in enemy_building_list:
                enemy_building_list[enemy_building_list.index(self.target)] = False
            self.target = None