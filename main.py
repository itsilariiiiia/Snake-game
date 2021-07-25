import pygame
import sys
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

class snake():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xspeed = 0
        self.yspeed = 0
        self.lenght = 1
        self.score = 0
        self.lastpositions = [[0, 0]]
        self.bestscore = 0
    def right(self):
        self.xspeed = 20 
        self.yspeed = 0
    def left(self):
        self.xspeed = -20
        self.yspeed = 0
    def up(self):
        self.xspeed = 0
        self.yspeed = -20
    def down(self):
        self.xspeed = 0
        self.yspeed = 20
    def updatelastpos(self):
        self.lastpositions.pop(0)
        self.lastpositions.append([self.x, self.y])
    def newhead(self):
        self.lastpositions.append([self.x, self.y])


player = snake()

with open(r"bestscore.txt", 'r') as infile:
    player.bestscore = int(infile.readlines()[0])


class obj():
    def randompoints(self):
        import random
        self.x = (random.randint(0, 29) * 20)
        self.y = (random.randint(0, 29) * 20)
        return [self.x, self.y]


def drawGrid(SCREEN):
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


def quit():
    with open(r"bestscore.txt", 'w') as infile:
        infile.write(str(max([player.score, player.bestscore])))
    pygame.quit()
    sys.exit()


def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    apple = obj()
    applecor = apple.randompoints()
    while 1:
        SCREEN.fill((0, 170, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.up()
                elif event.key == pygame.K_DOWN:
                    player.down()
                elif event.key == pygame.K_RIGHT:
                    player.right()
                elif event.key == pygame.K_LEFT:
                    player.left()
        player.x += player.xspeed
        player.y += player.yspeed
        if player.x > 600 or player.y > 600 or player.x < 0 or player.y < 0:
            quit()
        for item in player.lastpositions[1:]:
            if player.x == item[0] and player.y == item[1]:
                quit()
        if player.x == applecor[0] and player.y == applecor[1]:
            player.score += 1
            player.lenght += 1
            applecor = apple.randompoints()
            player.newhead()
        else:
            player.updatelastpos()
        drawGrid(SCREEN)
        pygame.draw.rect(SCREEN, (200, 0, 200), [player.x + 5, player.y + 5, 10, 10])
        if len(player.lastpositions) > 1:
            for item in player.lastpositions:
                pygame.draw.rect(SCREEN, (0, 0, 255), [item[0] + 5, item[1] + 5, 10, 10])
        pygame.draw.rect(SCREEN, (255, 0, 0), [applecor[0] + 5, applecor[1] + 5, 10, 10])
        SCREEN.blit(pygame.font.SysFont("comicsansms", 35).render("Score: " + str(player.score) + "   Best score: " + str(max([player.score, player.bestscore])), True, (200, 0, 0)), [0,0])
        pygame.display.update()
        clock.tick(10)




if __name__ == '__main__':
    main()