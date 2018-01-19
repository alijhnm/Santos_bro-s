import pygame, sys, random,time
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
pygame.init()
title_image = pygame.image.load('start.jpg')
game_over_image = pygame.image.load('end.jpg')
windowWidth = 711
windowHeight = 711
surface = pygame.display.set_mode((windowWidth,
windowHeight))
pygame.display.set_caption('Drop!')
leftDown = False
rightDown = False
gameStarted = False
gameEnded = False
gamePlatforms = []
platformSpeed = 3
platformDelay = 1000
lastPlatform = 0
platformsDroppedThrough = -1
dropping = False
gameBeganAt = 0
timer = 0
player = {'x' : windowWidth // 2,'y' : 0,'height' : 25,'width' : 25,'vy' : 3,'vx' : 5}
def drawPlayer():
    pygame.draw.rect(surface, (255,0,0), (player['x'],player['y'], player['width'], player['height']))
def movePlayer():
    global platformsDroppedThrough, dropping
    leftOfPlayerOnPlatform = True
    rightOfPlayerOnPlatform = True
    if player['x']  >= windowWidth - player['width'] :
        player['x'] = windowWidth - player['width'] - 1
    if surface.get_at((player['x'], player['y'] + player['height'])) == (0,0,0,255):
        leftOfPlayerOnPlatform = False
    if surface.get_at((player['x'] + player['width'], player['y'] + player['height'])) == (0,0,0,255):
        rightOfPlayerOnPlatform = False
    if not (rightOfPlayerOnPlatform and leftOfPlayerOnPlatform) and player['y'] + player['height'] + player['vy'] < windowHeight:
        player['y'] += player['vy']
        if dropping is False:
            dropping = True
            platformsDroppedThrough += 1
    else :
        foundPlatformTop = False
        yOffset = 0
        dropping = False
        while  not foundPlatformTop:
            if surface.get_at((player['x'], player['y'] + player['height'] - yOffset )) == (0,0,0,255) and \
                    surface.get_at((player['x'] + player['width'], player['y'] + player['height'] - yOffset)) == (0, 0, 0, 255):
                player['y'] -= yOffset
                foundPlatformTop = True
            elif player['y'] + player['height'] - yOffset > 0:
                yOffset += 1
            else:
                gameOver()
                break
    if leftDown is True:
        if player['x'] > 0 and player['x'] - 1 > 0:
            player['x'] -= player['vx']
        elif player['x'] > 0 and player['x'] - 1 < 0:
            player['x'] = 0
    if rightDown is True:
        if player['x'] + player['width'] < windowWidth and (player['x'] + player['width']) + 5 < windowWidth:
            player['x'] += player['vx']
        elif player['x'] + player['width'] < windowWidth and (player['x'] + player['width']) + 5 > windowWidth:
            player['x'] = windowWidth - player['width']
def createPlatform():
    global lastPlatform, platformDelay
    platformY = windowHeight
    gapPosition = random.randint(0, windowWidth - player['width']-10)
    gamePlatforms.append({'pos' : [0, platformY],'gap' : gapPosition})
    lastPlatform = GAME_TIME.get_ticks()
    if platformDelay > 800:
        platformDelay -= 50
def movePlatforms():
    # print(“Platforms”)
    for idx, platform in enumerate(gamePlatforms):
        platform['pos'][1] -= platformSpeed
        if platform['pos'][1] < -10:
            gamePlatforms.pop(idx)
def drawPlatforms():
    for platform in gamePlatforms:
        pygame.draw.rect(surface, (255,255,255), (platform['pos'][0], platform['pos'][1], windowWidth, 10))
        pygame.draw.rect(surface, (0,0,0), (platform['gap'],platform['pos'][1], player['width'] * 2, 10))
def gameOver():
    global gameStarted, gameEnded, platformsDroppedThrough
    platformSpeed = 0
    gameStarted = False
    gameEnded = True
    print(platformsDroppedThrough)
def restartGame():
    global gamePlatforms, player, gameBeganAt,platformsDroppedThrough, platformDelay
    gamePlatforms = []
    player['x'] = windowWidth // 2
    player['y'] = 0
    gameBeganAt = GAME_TIME.get_ticks()
    platformsDroppedThrough = -1
    platformDelay = 2000
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
            if event.key == pygame.K_SPACE:
                if gameStarted == False:
                    restartGame()
                    gameStarted = True
        if event.type == GAME_GLOBALS.QUIT:
            quitGame()
# ‘main’ loop
while True:
    surface.fill((0,0,0))
    check_events()
    if gameStarted is True: # Play game
        timer = GAME_TIME.get_ticks() - gameBeganAt
        movePlatforms()
        drawPlatforms()
        movePlayer()
        drawPlayer()
    elif gameEnded is True: # Draw game over screen
        surface.blit(game_over_image, (0, 150))
    else : # Welcome Screen
        surface.blit(title_image, (0, 150))
    if GAME_TIME.get_ticks() - lastPlatform > platformDelay:
        createPlatform()
    time.sleep(0.02)
    pygame.display.update()