import pygame
from pygame.locals import *
import time


class Main:
    def __init__(self, screen):
        self.running = True
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.devTool = False
        self.player = Player()
    # DevTools (Remove after beta)
    def devTools(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_F1]:
            self.devTool = True
        if keys[pygame.K_F2]:
            self.devTool = False
    def display(self):
        self.player.display(self.screen)
    def run(self):
        devTool = self.devTools()
        while self.running:
            screen.fill((0,0,0))
            self.devTools()
            self.display()
            self.player.move()
            self.player.borders()
            if self.devTool:
                mousex, mousey = pygame.mouse.get_pos()
                font = pygame.font.Font(None, 46)
                mousePos = font.render(f'{mousex}, {mousey}', True, (255, 255, 255))
                screen.blit(mousePos, (25, 25))
                self.cursor = pygame.Surface((10, 10))
                self.cursor.fill((255, 255, 255))
                self.bulletMask = pygame.mask.from_surface(self.cursor) 
                self.pos = pygame.mouse.get_pos()
                screen.blit(self.cursor, self.pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
            self.clock.tick(30)

class Player:
    def __init__(self) -> None:
        self.test = True
        self.player = pygame.image.load("monkey.png")
        self.velocity = [0, 0] # X, Y
        self.speed = 15
        self.position = [0, 0]
        self.mask = pygame.mask.from_surface(self.player)
    def display(self, screen):
        screen.blit(self.player, self.position)
    def move(self):
        keys = pygame.key.get_pressed()
        # X moves
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity[0] = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity[0] = 1
        else:
            self.velocity[0] = 0
        # Y moves
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.velocity[1] = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.velocity[1] = 1
        else:
            self.velocity[1] = 0
        self.position[0] += self.velocity[0] * self.speed
        self.position[1] += self.velocity[1] * self.speed
    def borders(self):
        if self.position[0] <= 0:
            self.position[0] = 0
        if self.position[0] >= 1080 - 64:
            self.position[0] = 1080 -64
        if self.position[1] <= 0:
            self.position[1] = 0
        if self.position[1] >= 720 - 128:
            self.position[1] = 720 - 128
    def hitbox(self):
        return self.mask.get_bounding_rects()[0].move(self.position)



pygame.init()

x = 1080
y = 720

screen = pygame.display.set_mode((x, y))

main = Main(screen)
main.run()

pygame.quit()
