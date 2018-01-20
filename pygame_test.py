import pygame,sys,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
pygame.init()
class Board:

    width = 800
    height = 800
    color = (0,0,0)
    mid_color = (255,255,255)
    mid_width = 40
    mid_offset = 100
    window = pygame.display.set_mode((width,height))

    def show(self):
        self.window.fill(self.color)
        print('Done!')
        pygame.draw.rect(self.window,self.mid_color,(self.mid_offset,self.height//2 - self.mid_width//2,self.width - 2 * self.mid_offset,self.mid_width))
        pygame.display.update()
        time.sleep(0.1)

class Card():
    
def get_events():
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitgame()

def quitgame():
    pygame.quit()
    sys.exit()
board = Board()

# Main Loop

while True:
    get_events()
    board.show()



