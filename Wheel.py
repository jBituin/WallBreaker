import pygame, random

# Fetch all images and store in array
def LoadImages(path, count):
    images = []
    for i in range(count):
        image = pygame.image.load(path % (str(i))).convert()
        image = pygame.transform.scale(image, (25, 25))
        images.append(image)
    return images


# Get screen configuration from Main.py
def GetScreen():
    from TapTapGame import Main
    return Main.screen


def GetBackground():
    from TapTapGame import Main
    return Main.background


direction = [1, -1]
# Yung sa gitna . Ewan ko cLass name . HAHAHA !
class Mastermind(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.screen = GetScreen()
        self.image = pygame.Surface((75, 75))
        self.image = self.image.convert()
        self.image.fill((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))

        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen.get_width() / 2
        self.rect.centery = self.screen.get_height() / 2

        self.currentFrame = 0
        self.animationFrame = 6

    def update(self):
        self.updateColor()

    def updateColor(self):
        self.currentFrame += 1
        if self.currentFrame >= self.animationFrame:
            self.currentFrame = 0
            self.image.fill((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))


# Class for mobs
class Mobs(Mastermind):

    def __init__(self):
        super().__init__()
        self.screen = GetScreen()
        self.images = LoadImages("C:/Users/Administrator/PycharmProjects/2DGame/TapTapGame/Resources/FireT_%s.png", 6)#Pass directory of images

        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

        # Spawn coordinates -- Around Mastermind
        self.rect.centerx = random.randrange(self.screen.get_width() / 2 - 75, self.screen.get_width() / 2 + 75)
        self.rect.centery = random.randrange(self.screen.get_height() / 2 - 75, self.screen.get_height() / 2 + 75)

        self.width = self.rect.width
        self.height = self.rect.height

        # Random speed
        self.dx = random.randint(-3, 3)
        self.dy = random.randint(-3, 3)

        # Number of images in the directory
        self.animationFrame = 6
        self.currentFrame = 0

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        #self.reverse()
        self.updateFrame()

    # Prevents the mob from passing through the screen
    # Also the method that damages the wall
    def reverse(self, direction):
        #if self.rect.right >= self.screen.get_width() or self.rect.left <= 0:
        if direction == "X":
            self.dx = self.dx * -1

        #if self.rect.top >= self.screen.get_height() - 40 or self.rect.bottom <= 25:
        if direction == "Y":
            self.dy = self.dy * -1

            print(self.dx, self.dy)

    # Changes image every 6 tick
    def updateFrame(self):
        self.currentFrame += 1

        if self.currentFrame >= self.animationFrame:
            self.currentFrame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]


class Aids(Mastermind):
    choice = [-8, -7, -6, 6, 7, 8]

    def __init__(self):
        super().__init__()

        self.screen = GetScreen()
        self.image = pygame.Surface((25, 25))
        self.image = self.image.convert()
        self.image.fill((0, 0, 255))

        self.rect = self.image.get_rect()

        self.rect.centerx = random.randrange(self.screen.get_width() / 2 - 75, self.screen.get_width() / 2 + 75)
        self.rect.centery = random.randrange(self.screen.get_height() / 2 - 75, self.screen.get_height() / 2 + 75)

        self.dx = random.choice(self.choice)
        self.dy = random.choice(self.choice)

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        #self.reverse()

    def reverse(self, direction):
        #if self.rect.right >= self.screen.get_width() or self.rect.left <= 0:
        if direction == "X":
            self.dx = self.dx * -1

        #if self.rect.top >= self.screen.get_height() - 25 or self.rect.bottom <= 25:
        if direction == "Y":
            self.dy = self.dy * -1


class Healer(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.screen = GetScreen()
        self.images = LoadImages("C:/Users/Administrator/PycharmProjects/2DGame/TapTapGame/Resources/heal (%s).png", 24)#Pass directory of images

        self.images = [pygame.transform.scale(image, (25, 25)) for image in self.images]
        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

        # Spawn coordinates -- Around Mastermind
        self.rect.centerx = random.randrange(self.screen.get_width() / 2 - 75, self.screen.get_width() / 2 + 75)
        self.rect.centery = random.randrange(self.screen.get_height() / 2 - 75, self.screen.get_height() / 2 + 75)

        self.width = self.rect.width
        self.height = self.rect.height

        # Random speed
        self.dx = random.randint(-3, 3)
        self.dy = random.randint(-3, 3)

        # Number of images in the directory
        self.animationFrame = 24
        self.currentFrame = 0

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        #self.reverse()
        self.updateFrame()

    # Prevents the mob from passing through the screen
    # Also the method that heals the wall
    def reverse(self, direction):
        #if self.rect.right >= self.screen.get_width() or self.rect.left <= 0:
        if direction == "X":
            self.dx = self.dx * -1

        #if self.rect.top >= self.screen.get_height() - 25 or self.rect.bottom <= 25:
        if direction == "Y":
            self.dy = self.dy * -1

    # Changes image every 6 tick
    def updateFrame(self):
        self.currentFrame += 1

        if self.currentFrame >= self.animationFrame:
            self.currentFrame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
            self.image = self.image.convert()


class Label(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 30)
        self.text = ""
        self.center = (320, 240)

    def update(self):
        self.image = self.font.render(self.text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center


class Wall(pygame.sprite.Sprite):
    HP = 100
    def __init__(self, height, width, xPos, yPos):
        super().__init__()
        self.screen = GetScreen()
        self.image = GetBackground()
        self.xPos = xPos
        self.yPos = yPos

        pygame.draw.rect(self.image, (255, 0, 255), (xPos, yPos, width, height))
        self.rect = pygame.Rect(xPos, yPos, width, height)
