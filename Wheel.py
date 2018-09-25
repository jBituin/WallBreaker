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
    import Main
    return Main.screen


def GetBackground():
    import Main
    return Main.background


direction = [1, -1]
class Mastermind(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.screen = GetScreen()
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
        self.screen = GetScreen()
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

        self.screen = GetScreen()
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
        self.screen = GetScreen()
        self.images = LoadImages("Resources/leaf%s.png", 4)#Pass directory of images
        #self.images = LoadImages("H:/2DGame/TapTapGame/Resources/healFX(%s).png", 6)
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
        self.screen = GetScreen()
        self.width = width
        self.height = height
        self.imageGreen = pygame.image.load("Resources/Wall.jpg")
        #self.image = pygame.image.load("H:/2DGame/TapTapGame/Resources/Blocks/leavesBlock.png")
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
        self.screen = GetScreen()
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