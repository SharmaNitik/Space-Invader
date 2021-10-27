import pygame, random, math, player
from pygame import mixer
#initialising pygame
pygame.init()
#initialising display
screenX = 1200
screenY= 600
screen = pygame.display.set_mode((screenX, screenY))

# adding title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# adding background 
background = pygame.image.load("background.png")

# adding sound and music
mixer.music.load("background.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.3)

# creating font for scoreboard and Game_over
font = pygame.font.Font('freesansbold.ttf', 32)
game = pygame.font.Font('freesansbold.ttf', 80)
game_over = game.render(("Game Over"), True, (255,255,255))

def scoreboard():
    score = font.render(("Score :"+ str(count)), True, (255,255,255))
    screen.blit(score, (0,0))

# collision
def collision(enemyX, bulletX, enemyY, bulletY):
    dist = math.sqrt((enemyX-bulletX)**2 + (enemyY-bulletY)**2)
    if dist<30:
        collision = mixer.Sound("explosion.wav")
        collision.play()
        return True
    else:
        return False



#initial coordinates of enemy to screen
enemyX = random.randint(0,screenX-64)
enemyY = random.randint(0,screenY/3)
enemyimg = pygame.image.load("enemy.png")
enemyX_change = 4
enemyY_change = 40

#initial coordinates of bullet to screen
bulletX = -3
bulletY = -3
bulletY_change = 0
bulletimg = pygame.image.load("bullet.png")

count = 0
running = True
fire = "ready"
while(running):

    # adding background to screen
    screen.blit(background, (0, 0))
    # adding player to screen
    screen.blit(playerimg, (playerX, playerY))
    # adding enemy to screen
    screen.blit(enemyimg, (enemyX, enemyY))

    # evemt listener   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_LEFT:
                playerX_change = -8
            if event.key == pygame.K_RIGHT:
                playerX_change =  8
            if event.key == pygame.K_SPACE:
                if(fire=="ready"):
                    fire = "unready"
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    bulletY =  screenY * 0.9 + 20
                    bulletY_change = -20

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            
    # player coordinates updater
    playerX += playerX_change
    if playerX >= screenX-64:
        playerX = screenX-64
    if playerX <= 0:
        playerX = 0
    screen.blit(playerimg,(playerX, playerY))

    # enemy coordinates updater
    enemyX += enemyX_change
    if (enemyX >= screenX-64):
        enemyX = screenX - 64
        enemyX_change *= -1
        enemyY += enemyY_change
    if (enemyX <= 0):
        enemyX = 0
        enemyX_change *= -1
        enemyY += enemyY_change
    if enemyY >= playerY:
        screen.blit(game_over,(screenX/3-60, screenY/2-30))
        
    bulletY += bulletY_change
    if bulletY <= 0:
        fire = "ready"
    if collision(enemyX, bulletX, enemyY, bulletY):
        fire = "ready"
        count += 1
        enemyX = random.randint(0,screenX-64)
        enemyY = random.randint(0,screenY/3)
    screen.blit(bulletimg,(bulletX, bulletY))
    scoreboard()
    # screen updater
    pygame.display.update()


