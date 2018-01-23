import pygame,sys,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import Functions
pygame.init()
low_speed = 5
medium_speed = 6.25
fast_speed = 7.5
small_size = 40
medium_size = 50
big_size = 60
AttackRange = 5
small_area_of_effect = 40
medium_area_of_effect = 50
large_area_of_effect = 60
enemy_card_list = []
enemy_building_list = []

window = pygame.display.set_mode((800,800))
enemy_list = [True,True,True]

class Card:
    '''Doc for Card class'''
    def __init__(self,MaxHealth,Speed,AttackDamage,Type,TargetType,AttackRange,AttackInterval,AreaOfEffect,Size):
        self.x = None
        self.y = None
        self.max_health = MaxHealth
        self.hp = MaxHealth
        self.speed = Speed
        self.attack_damage = AttackDamage
        self.type = Type
        self.target_type = TargetType
        self.attack_range = AttackRange
        self.attack_interval = AttackInterval
        self.deploy_time = 1000
        self.area_of_effect = AreaOfEffect
        self.size = Size
        self.elixir_cost = None
    def move(self,game):
        '''Doc for move function
        if self.y >  game.height / 2:
            if self.x < game.width / 2:
                destination = (0,game.height // 2)
                if self.x - self.speed // 2 >= destination[0]:
                    self.x -= self.speed
                else:

                if self.y - self.speed // 2 >= destination[1]:
                    self.y -= self.speed
        '''
    def show(self,window):
        window.blit(self.image,(self.x,self.y))

class Barbarian(Card):
    '''Doc for Barbarian'''
    def __init__(self,X,Y):
        Card.__init__(self,636,medium_speed,159,'Ground','Ground','Melee',1500,False,medium_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 2
        self.image = pygame.image.load('Barrel.png')

class Archer(Card):
    '''Doc for Archer'''
    def __init__(self,X,Y):
        Card.__init__(self,254,medium_speed,86,'Ground','Air $ Ground',5 * AttackRange,1200,False,small_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 2

class Giant(Card):
    '''Doc for Giant'''
    def __init__(self, X, Y, ElixirCost):
        Card.__init__(self, 3344, low_speed, 211, 'Ground', 'Building', 'Melee', 1500,
                      'False', big_size)
        self.x = X
        self.y = Y
        self.elixir_cost = ElixirCost

class Dragon(Card):
    '''Doc for Dragon'''
    def __init__(self, X, Y):
        Card.__init__(self, 1064, fast_speed, 133, 'Air', 'Air $ Ground', 3.5 * AttackRange, 1600, small_area_of_effect, medium_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 4


class PEKKA(Card):
    '''Doc for PEKKA'''
    def __init__(self, X, Y):
        Card.__init__(self, 3458, low_speed, 678, 'Ground', 'Ground', 'Melee', 1800,False, big_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 7


class Ballon(Card):
    '''Doc for Ballon'''
    def __init__(self, X, Y):
        Card.__init__(self, 798, medium_speed, 798, 'Air', 'Building', 'Melee', 3000,medium_area_of_effect, big_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 5


class Miner(Card):
    '''Doc for Miner'''
    def __init__(self, X, Y):
        Card.__init__(self, 1000, fast_speed, 160, 'Ground', 'Ground', 'Melee', 1200,False, medium_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 3


class Building:
    '''Doc for Building'''
    def __init__(self,X,Y,MaxHealth,AttackDamage,AttackRange,AttackInterval,AreaOfEffect,Address):
        self.x = X
        self.y = Y
        self.max_health = MaxHealth
        self.current_health = MaxHealth
        self.attack_damage = AttackDamage
        self.attack_range = AttackRange
        self.attack_interval = AttackInterval
        self.area_of_effect = AreaOfEffect
        self.image = pygame.image.load(Address)

    def show(self,window):
           window.blit(self.image,(self.x,self.y))

