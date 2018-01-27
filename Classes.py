import pygame,sys,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import Functions,Constants
pygame.init()

#General Card class
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
        self.target = None
        self.attack_image = None
        self.move_up_image = None
        self.move_down_image = None
        self.last_attack = 0
        self.team_color = (0,0,255)

    def show(self,window,image):
        window.blit(self.move_up_image,(self.x,self.y))
        pygame.draw.rect(window,(100,100,100),(self.x,self.y - Constants.hp_bar_offset,self.size,Constants.hp_bar_width))
        pygame.draw.rect(window,self.team_color,(self.x,self.y - Constants.hp_bar_offset,int(self.hp / self.max_health * self.size),Constants.hp_bar_width))

    def attack(self,time,window,enemy_team):
        if time - self.last_attack > self.attack_interval:
            self.target.hp -= self.attack_damage
            self.last_attack = time
            window.blit(self.move_up_image,(self.x,self.y))
            pygame.draw.line(window,(255,0,0),(self.x + self.size//2,self.y + self.size//2),(self.target.x + self.target.size//2,self.target.y + self.target.size//2))
            if self.target.hp <= 0:
                enemy_team.remove(self.target)
                self.target = None
        else:
            window.blit(self.move_up_image,(self.x,self.y))

class Barbarian(Card):
    '''Doc for Barbarian'''
    def __init__(self,X,Y):
        Card.__init__(self,636,Constants.medium_speed,159,'Ground','Ground','Melee',1500,False,Constants.medium_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 2
        self.move_up_image = pygame.image.load('Barrel.png')
        self.attack_image = pygame.image.load('Archer.png')



class Archer(Card):
    '''Doc for Archer'''
    def __init__(self,X,Y):
        Card.__init__(self,254,Constants.medium_speed,86,'Ground','Air $ Ground',5 * Constants.AttackRange,1200,False,Constants.small_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 2
        self.move_up_image = pygame.image.load('Archer1.png')


class Giant(Card):
    '''Doc for Giant'''
    def __init__(self, X, Y):
        Card.__init__(self, 3344, Constants.low_speed, 211, 'Ground', 'Building', 'Melee', 1500,
                      'False', Constants.big_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 5
        self.move_up_image = pygame.image.load('Giant2.png')

class Dragon(Card):
    '''Doc for Dragon'''
    def __init__(self, X, Y):
        Card.__init__(self, 1064, Constants.fast_speed, 133, 'Air', 'Air $ Ground', 3.5 * Constants.AttackRange, 1600, Constants.small_area_of_effect, Constants.medium_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 4
        self.move_up_image = pygame.image.load('dragon2.png')

class PEKKA(Card):
    '''Doc for PEKKA'''
    def __init__(self, X, Y):
        Card.__init__(self, 3458, Constants.low_speed, 678, 'Ground', 'Ground', 'Melee', 1800,False, Constants.big_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 7
        self.move_up_image = pygame.image.load('peka2.png')


class Ballon(Card):
    '''Doc for Ballon'''
    def __init__(self, X, Y):
        Card.__init__(self, 798, Constants.medium_speed, 798, 'Air', 'Building', 'Melee', 3000,Constants.medium_area_of_effect, Constants.big_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 5
        self.move_up_image = pygame.image.load('dragon1.png')


class Hog(Card):
    '''Doc for Miner'''
    def __init__(self, X, Y):
        Card.__init__(self, 1000, Constants.fast_speed, 160, 'Ground', 'Ground', 'Melee', 1200,False, Constants.medium_size)
        self.x = X
        self.y = Y
        self.elixir_cost = 4
        self.move_up_image = pygame.image.load('hog1.png')

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
        self.target = None
        self.size = 100
        self.last_hit = 0

    def show(self,window):
        window.blit(self.image,(self.x,self.y))

    def attack(self,time,window,enemy_team):
        if time - self.last_hit > self.attack_interval:
            self.target.hp -= self.attack_damage
            self.last_hit = time
            pygame.draw.line(window, (255, 255, 255), (self.x + self.size//2, self.y + self.size//2),
                             (self.target.x + self.target.size//2, self.target.y + self.target.size//2))
        if self.target.hp <= 0:
            enemy_team.remove(self.target)
            self.target = None

