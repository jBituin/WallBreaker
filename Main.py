#Initialization
import pygame, random
from Wheel import *

pygame.init()
pygame.mixer.init()

# Sprite Groups
allSprites = pygame.sprite.Group()
mobGroup = pygame.sprite.Group()
aidGroup = pygame.sprite.Group()
healGroup = pygame.sprite.Group()
movingGroup = pygame.sprite.Group()
wallGroup = pygame.sprite.Group()

#BG Music
menuSound = pygame.mixer.Sound("Resources/main menu bgm.ogg")
gamePlaySound = pygame.mixer.Sound("Resources/gameplay.ogg")
gameOverSound = pygame.mixer.Sound("Resources/gameover.ogg")

#General Text
text = pygame.font.SysFont("Century Gothic", 50)
# Display configuration
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("2D")

ibil = Mastermind()

scoreText = Label(screen.get_width() - 75, 13, 30, (255, 255, 255))
wallHP = Label(screen.get_width() / 2, screen.get_height() / 2 - 50, 30, (255, 255, 255))

# Wall creations
wallLeft = Wall(screen.get_height() - 50, 25, 0, 25)
wallTop = Wall(25, screen.get_width() - 50, 25, 0)
wallRight = Wall(screen.get_height() - 50, 25, screen.get_width() - 25, 25)
wallBottom = Wall(25, screen.get_width() - 50, 25, screen.get_height() - 25)

# background = pygame.Surface(screen.get_size())
background = pygame.image.load('Resources/bg.png')
background = pygame.transform.scale(background, screen.get_size())
background = background.convert()

clock = pygame.time.Clock()

score = 0
bestScore = 0

def GetBestScore():
    # Default high score
    bestScore = 0

    # Try to read the high score from a file
    try:
        bestScore_file = open("best.txt", "r")
        bestScore = int(bestScore_file.read())
        bestScore_file.close()
        print("The high score is", bestScore)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")

    return bestScore

def SetBestScore(newBest):
    try:
        # Write the file to disk
        bestScore_file = open("best.txt", "w")
        bestScore_file.write(str(newBest))
        bestScore_file.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")


#Adds Enemy
def SpawnEnemy():
    enemy = Mobs()
    allSprites.add(enemy)
    mobGroup.add(enemy)
    movingGroup.add(enemy)

#Adds Aid
def SpawnAid():
    aid = Aids()
    allSprites.add(aid)
    aidGroup.add(aid)
    movingGroup.add(aid)

def SpawnHealer():
    healer = Healer()
    allSprites.add(healer)
    healGroup.add(healer)
    movingGroup.add(healer)

#Remove sprite from all sprite groups
def Kill(sprite):
    sprite.kill()
    allSprites.remove(sprite)
    movingGroup.remove(sprite)

    if isinstance(sprite, Mobs):
        mobGroup.remove(sprite)

    elif isinstance(sprite, Aids):
        aidGroup.remove(sprite)

    elif isinstance(sprite, Healer):
        healGroup.remove(sprite)

def GetHP():
    totalHP = 0
    for wall in wallGroup:
        totalHP += wall.HP

    return totalHP

def GameOver():
    gamePlaySound.stop()
    gameOverSound.play(-1)

    global score, bestScore

    bestScore = GetBestScore()

    print("Score",score, "best score", bestScore)
    if score > bestScore:
        SetBestScore(score)

    wallHP.text = "Game Over"
    movingGroup.empty()
    wallGroup.empty()
    allSprites.empty()
    aidGroup.empty()
    mobGroup.empty()
    healGroup.empty()

    fireBG = pygame.image.load('Resources/fire.jpg')
    fireBG = pygame.transform.scale(fireBG, screen.get_size())
    fireBG = fireBG.convert()

    playText = text.render("Retry", 1, (255, 255, 255))
    quitText = text.render("Quit", 1, (255, 255, 255))
    gameOverText = text.render("GAME OVER", 1, (255, 255, 255))
    bestText = text.render("Best: " + str(GetBestScore()), 1, (255, 255, 255))


    retry = False
    while not retry:
        screen.blit(fireBG, (0, 0))
        screen.blit(bestText, (10, 10))
        screen.blit(gameOverText, (215, 190))
        screen.blit(playText, (270, 240))
        screen.blit(quitText, (275, 290))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse1, mouse2 = pygame.mouse.get_pos()

                if mouse1 >= 260 and mouse1 <= 350 and mouse2 >= 240 and mouse2 <= 290:
                    retry = True
                    score = 0
                    gameOverSound.stop()
                    Main()

                elif mouse1 >= 260 and mouse1 <= 350 and mouse2 >= 290 and mouse2 <= 340:
                    pygame.quit()
                    quit()

        clock.tick(60)
        pygame.display.flip()

def MenuScreen():
    menuSound.play(-1)

    sampleGroup = pygame.sprite.Group()
    fire = Display("Resources/FireT_%s.png", 6, 110, 350)
    ice = Display("Resources/iceball (%s).png", 6, 110, 380)
    heal = Display("Resources/leaf%s.png", 4, 110, 410)

    play = False
    fireText = Label(300, 350, 20, (255, 0, 0))
    fireText.text = "Damages the walls (Click these !!!)"

    iceText = Label(343, 380, 20, (0, 0, 255))
    iceText.text = "Destroys all fires (Click these to destroy fires !!!)"

    healText = Label(295, 410, 20, (30, 255, 30))
    healText.text = "Heals the walls (Don't destroy !!!)"

    text = pygame.font.SysFont("Arial", 50)
    wall = pygame.font.SysFont("Lato", 100)
    Breaker = pygame.font.SysFont("Lato", 100)

    sampleGroup.add(fire, ice, heal, fireText, iceText, healText)

    playText = text.render("Play", 1, (0, 0, 0))
    instructionText = text.render("Click objects to destroy", 1, (0, 0, 0))
    bestText = text.render("Best: " + str(GetBestScore()), 1, (0, 0, 0))

    while not play:
        wallText = wall.render("Wall", 1, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        breakerText = Breaker.render("Breaker", 1, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))

        screen.blit(background, (0, 0))
        screen.blit(bestText, (10, 10))
        screen.blit(wallText, (250, 80))
        screen.blit(breakerText, (200, 140))
        screen.blit(playText, (260, 240))
        screen.blit(instructionText, (120, 280))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse1, mouse2 = pygame.mouse.get_pos()

                if mouse1 >= 260 and mouse1 <= 340 and mouse2 >= 240 and mouse2 <= 300:
                    play = True

        sampleGroup.clear(screen, background)
        sampleGroup.update()
        sampleGroup.draw(screen)

        clock.tick(60)
        pygame.display.flip()


def Main():
    # The one in the center

    gamePlaySound.play(-1)
    allSprites.add(wallLeft, wallTop, wallRight, wallBottom, ibil, scoreText, wallHP)
    wallGroup.add(wallLeft, wallTop, wallRight, wallBottom)

    for wall in wallGroup:
        wall.HP = 125

    global score
    mobRange = 5
    aidRange = 1
    healRange = 1
    scoreFlag = 0

    keepGoing = True

    # Main Loop
    while keepGoing:
        screen.blit(background, (0, 0))
        scoreText.text = "Score: " + str(score)

        wallHP.text = "HP" + str(GetHP())

        ### SPAWN CHANCE ###
        mobChance = random.randrange(500)
        aidChance = random.randrange(1000)
        healChance = random.randrange(1000)

        if mobChance < mobRange:
            SpawnEnemy()

        if aidChance < aidRange:
            if len(aidGroup) < 2:
                SpawnAid()

        if healChance < healRange:
            if len(healGroup) < 2:
                SpawnHealer()
        ### SPAWN CHANCE ###

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse1, mouse2 = pygame.mouse.get_pos()  # Get Mouse coordinates

                for obj in movingGroup:
                    if mouse1 >= obj.rect.left and mouse1 <= obj.rect.right and mouse2 >= obj.rect.top and mouse2 <= obj.rect.bottom:
                        Kill(obj)
                        if isinstance(obj, Mobs):
                            score += 1
                            scoreFlag += 1

                        elif isinstance(obj, Aids):
                            for e in mobGroup:
                                Kill(e)
                                score += 1
                                scoreFlag += 1

        for wall in wallGroup:
            for obj in movingGroup:
                if wall.rect.colliderect(obj.rect):
                    if wall == wallLeft or wall == wallRight:
                        obj.reverse("X")

                    elif wall == wallTop or wall == wallBottom:
                        obj.reverse("Y")

                    if isinstance(obj, Mobs):
                        wall.HP -= 10

                    if isinstance(obj, Healer):
                        wall.HP += 75

        if scoreFlag >= 15:
            mobRange += 1.5
            aidRange += .4
            healRange += .4
            scoreFlag = 0

        if GetHP() <= 0:
            GameOver()
            keepGoing = False

        ### UPDATE SPRITES ###
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        ### UPDATE SPRITES ###

        clock.tick(60)

        pygame.display.flip()

MenuScreen()
menuSound.stop()
Main()

pygame.time.delay(2000)
pygame.quit()
quit()

