#Initialization
import pygame, random

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


def LoadImages(path, count):
    images = []
    for i in range(count):
        image = pygame.image.load(path % (str(i))).convert()
        image = pygame.transform.scale(image, (25, 25))
        images.append(image)
    return images

direction = [1, -1]
class Mastermind(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.screen = screen
        self.images = LoadImages("Resources/portal (%s).png", 3)
        self.images = [pygame.transform.scale(image, (100, 100)) for image in self.images]
        self.index = 0

        self.image = self.images[self.index]

        '''self.image = pygame.Surface((75, 75))
        self.image = self.image.convert()
        self.image.fill((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))'''

        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen.get_width() / 2
        self.rect.centery = self.screen.get_height() / 2

        self.currentFrame = 0
        self.animationFrame = 6

    def update(self):
        self.updateColor()

    def updateColor(self):
        '''self.currentFrame += 1
        if self.currentFrame >= self.animationFrame:
            self.currentFrame = 0
            self.image.fill((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))'''

        self.currentFrame += 1

        if self.currentFrame >= self.animationFrame:
            self.currentFrame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]


# Class for mobs
class Mobs(Mastermind):
    choice = [-5, -4, -3, 3, 4, 5]

    def __init__(self):
        super().__init__()
        self.screen = screen
        self.images = LoadImages("Resources/FireT_%s.png", 6)#Pass directory of images
        self.images = [pygame.transform.scale(image, (50, 50)) for image in self.images]
        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

        # Spawn coordinates -- Around Mastermind
        self.rect.centerx = random.randrange(self.screen.get_width() / 2 - 75, self.screen.get_width() / 2 + 75)
        self.rect.centery = random.randrange(self.screen.get_height() / 2 - 75, self.screen.get_height() / 2 + 75)

        self.width = self.rect.width
        self.height = self.rect.height

        # Random speed
        self.dx = random.choice(self.choice)
        self.dy = random.choice(self.choice)

        # Number of images in the directory
        self.animationFrame = 6
        self.currentFrame = 0

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        self.updateFrame()

    # Prevents the mob from passing through the screen
    # Also the method that damages the wall
    def reverse(self, direction):
        if direction == "X":
            self.dx = self.dx * -1

        if direction == "Y":
            self.dy = self.dy * -1

    # Changes image every 6 tick
    def updateFrame(self):
        self.currentFrame += 1

        if self.currentFrame >= self.animationFrame:
            self.currentFrame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]


class Aids(Mastermind):
    choice = [-7, -6, -4, 4, 6, 7]

    def __init__(self):
        super().__init__()

        self.screen = screen
        self.images = LoadImages("Resources/iceball (%s).png", 8)  # Pass directory of images
        self.images = [pygame.transform.scale(image, (50, 50)) for image in self.images]
        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

        # Spawn coordinates -- Around Mastermind
        self.rect.centerx = random.randrange(self.screen.get_width() / 2 - 75, self.screen.get_width() / 2 + 75)
        self.rect.centery = random.randrange(self.screen.get_height() / 2 - 75, self.screen.get_height() / 2 + 75)

        self.width = self.rect.width
        self.height = self.rect.height

        # Random speed
        self.dx = random.choice(self.choice)
        self.dy = random.choice(self.choice)

        # Number of images in the directory
        self.animationFrame = 6
        self.currentFrame = 0

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        self.updateFrame()
    def reverse(self, direction):
        if direction == "X":
            self.dx = self.dx * -1

        if direction == "Y":
            self.dy = self.dy * -1

    def updateFrame(self):
        self.currentFrame += 1

        if self.currentFrame >= self.animationFrame:
            self.currentFrame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]


class Healer(pygame.sprite.Sprite):
    choice = [-1, 1]

    def __init__(self):
        super().__init__()
        self.screen = screen
        self.images = LoadImages("Resources/leaf%s.png", 4)#Pass directory of images
        self.images = [pygame.transform.scale(image, (25, 25)) for image in self.images]
        self.images = [image.convert() for image in self.images]
        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

        # Spawn coordinates -- Around Mastermind
        self.rect.centerx = random.randrange(self.screen.get_width() / 2 - 75, self.screen.get_width() / 2 + 75)
        self.rect.centery = random.randrange(self.screen.get_height() / 2 - 75, self.screen.get_height() / 2 + 75)

        self.width = self.rect.width
        self.height = self.rect.height

        # Random speed
        self.dx = random.choice(self.choice)
        self.dy = random.choice(self.choice)

        # Number of images in the directory
        self.animationFrame = 24
        self.currentFrame = 0

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        #self.reverse()
        self.updateFrame()

    # Prevents the mob from passing through the screen
    def reverse(self, direction):
        if direction == "X":
            self.dx = self.dx * -1

        if direction == "Y":
            self.dy = self.dy * -1

    def updateFrame(self):
        self.currentFrame += 1

        if self.currentFrame >= self.animationFrame:
            self.currentFrame = 10
            self.animationFrame = 16
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
            self.image = self.image.convert()


class Label(pygame.sprite.Sprite):

    def __init__(self, xPos, yPos, size, color):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", size)
        self.text = ""
        self.center = (xPos, yPos)
        self.color = color

    def update(self):
        self.image = self.font.render(self.text, 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.center


class Wall(pygame.sprite.Sprite):
    HP = 125
    def __init__(self, height, width, xPos, yPos):
        super().__init__()
        self.screen = screen
        self.width = width
        self.height = height
        self.imageGreen = pygame.image.load("Resources/Wall.jpg")
        self.imageFire = pygame.image.load("Resources/wallFire.png")

        self.imageGreen = pygame.transform.scale(self.imageGreen, (width, height))
        self.imageFire = pygame.transform.scale(self.imageFire, (width, height))
        self.xPos = xPos
        self.yPos = yPos

        #pygame.draw.rect(self.image, (255, 0, 255), (xPos, yPos, width, height))
        self.rect = pygame.Rect(xPos, yPos, width, height)

    def update(self):
        if self.HP < 50:
            self.image = self.imageFire

        else:
            self.image = self.imageGreen


class Display(pygame.sprite.Sprite):

    def __init__(self, path, count, xPos, yPos):
        super().__init__()
        self.screen = screen
        self.images = LoadImages(path, count)#Pass directory of images
        self.images = [pygame.transform.scale(image, (50, 50)) for image in self.images]
        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

        # Spawn coordinates -- Around Mastermind
        self.rect.centerx = xPos
        self.rect.centery = yPos

        self.width = self.rect.width
        self.height = self.rect.height

        # Number of images in the directory
        self.animationFrame = count + 1
        self.currentFrame = 0

    def update(self):
        self.updateFrame()

    # Changes image every 6 tick
    def updateFrame(self):
        self.currentFrame += 1

        if self.currentFrame >= self.animationFrame:
            self.currentFrame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

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


    playText = text.render("Play", 1, (0, 0, 0))
    instructionText = text.render("Click objects to destroy", 1, (0, 0, 0))
    bestText = text.render("Best: " + str(GetBestScore()), 1, (0, 0, 0))

    copyrightText = Label(530, 470, 14, (255, 255, 255))
    copyrightText.text = "(c) Copyright Disclaimer. Credits to all images" 

    sampleGroup.add(fire, ice, heal, fireText, iceText, healText, copyrightText)

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

