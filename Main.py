#Initialization
import pygame, random

from pygame.sprite import Sprite

from TapTapGame.Wheel import Mastermind, Mobs, Aids, Healer, Wall

pygame.init()
pygame.mixer.init()

# Sprite Groups
allSprites = pygame.sprite.Group()
mobGroup = pygame.sprite.Group()
aidGroup = pygame.sprite.Group()
healGroup = pygame.sprite.Group()
movingGroup = pygame.sprite.Group()
wallGroup = pygame.sprite.Group()

# Display configuration
screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("2D")

# background = pygame.Surface(screen.get_size())
background = pygame.image.load('C:/Users/Administrator/PycharmProjects/2DGame/TapTapGame/Resources/bg.png')
background = pygame.transform.scale(background, screen.get_size())
background = background.convert()
# background.fill(BLACK)

clock = pygame.time.Clock()

# The one in the center
ibil = Mastermind()

# Wall creations
wallLeft = Wall(screen.get_height(), 25, 0, 0)
wallTop = Wall(25, screen.get_width(), 0, 0)
wallRight = Wall(screen.get_height(), 25, screen.get_width() - 25, 0)
wallBottom = Wall(25, screen.get_width(), 0, screen.get_height() - 25)

allSprites.add(wallLeft, wallTop, wallRight, wallBottom, ibil)
wallGroup.add(wallLeft, wallTop, wallRight, wallBottom)

mouse1 = mouse2 = 0

keepGoing = True
i = 0
for wall in wallGroup:
    print(i, wall.rect)
    i += 1

x = True
# Main Loop
while keepGoing:
    screen.blit(background, (0, 0))

    ### SPAWN CHANCE ###
    mobChance = random.randrange(100)
    aidChance = random.randrange(500)
    healChance = random.randrange(300)

    if mobChance < 5:
        enemy = Mobs()
        allSprites.add(enemy)
        mobGroup.add(enemy)
        movingGroup.add(enemy)

    '''if x:
        enemy = Mobs()
        allSprites.add(enemy)
        mobGroup.add(enemy)
        movingGroup.add(enemy)
        x = False'''

    if aidChance < 1:
        aid = Aids()
        allSprites.add(aid)
        aidGroup.add(aid)
        movingGroup.add(aid)

    if healChance < 1:
        healer = Healer()
        allSprites.add(healer)
        healGroup.add(healer)
        movingGroup.add(healer)
    ### SPAWN CHANCE ###

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse1, mouse2 = pygame.mouse.get_pos()  # Get Mouse coordinates

            for obj in mobGroup:
                # If the mobSprite is clicked -- Destroy
                if mouse1 >= obj.rect.left and mouse1 <= obj.rect.right and mouse2 >= obj.rect.top and mouse2 <= obj.rect.bottom:
                    obj.kill()
                    allSprites.remove(obj)
                    mobGroup.remove(obj)

            for obj in aidGroup:
                # if the aidSprite is clicked -- Destroy
                if mouse1 >= obj.rect.left and mouse1 <= obj.rect.right and mouse2 >= obj.rect.top and mouse2 <= obj.rect.bottom:
                    obj.kill()
                    allSprites.remove(obj)
                    aidGroup.remove(obj)

                    # Aid function undecided
                    # Kill all mobs on the screen -- Current Function
                    for mob in mobGroup:
                        mobGroup.remove(mob)
                        allSprites.remove(mob)

            for obj in healGroup:
                # If the mobSprite is clicked -- Destroy
                if mouse1 >= obj.rect.left and mouse1 <= obj.rect.right and mouse2 >= obj.rect.top and mouse2 <= obj.rect.bottom:
                    obj.kill()
                    allSprites.remove(obj)
                    healGroup.remove(obj)

    for wall in wallGroup:
        for obj in movingGroup:

            #print(type(obj))
            if wall.rect.colliderect(obj.rect):
                if wall == wallLeft or wall == wallRight:
                    obj.reverse("X")

                elif wall == wallTop or wall == wallBottom:
                    obj.reverse("Y")

                if isinstance(obj, Mobs):
                    wall.HP -= 1
                    print(wall.HP)

                if isinstance(obj, Healer):
                    wall.HP += .5
                    print(wall.HP)

    ### UPDATE SPRITES ###
    allSprites.clear(screen, background)
    allSprites.update()
    allSprites.draw(screen)
    ### UPDATE SPRITES ###

    clock.tick(60)

    pygame.display.flip()

pygame.quit()
quit()
