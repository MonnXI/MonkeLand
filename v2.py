import pygame
from pygame.locals import *
import sys
import time

pause = False

class Main:
    def __init__(self, screen):
        global pause
        self.pause = pause
        self.running = True
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.devTool = False
        self.player = Player()
        self.menu = Menu()
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
            if not self.pause:
                self.display()
                self.player.move()
                self.player.borders()
            else:
                self.menu.open(self.screen, self.pause)
            # DevTools actions
            if self.devTool:
                mousex, mousey = pygame.mouse.get_pos()
                font = pygame.font.Font(None, 46)
                mousePos = font.render(f'{mousex}, {mousey}', True, (255, 255, 255))
                self.clock.tick(70)
                fps = str(int(self.clock.get_fps()))
                fpsRender = font.render(f"{fps} FPS", True, (255, 255, 255))
                screen.blit(fpsRender, (540, 25))
                screen.blit(mousePos, (25, 25))
                self.cursor = pygame.Surface((10, 10))
                self.cursor.fill((255, 255, 255))
                self.cursorMask = pygame.mask.from_surface(self.cursor) 
                self.pos = pygame.mouse.get_pos()
                screen.blit(self.cursor, self.pos)
                self.offset = (self.pos[0] - self.player.position[0], self.pos[1] - self.player.position[1])
                if self.player.mask.overlap(self.cursorMask, self.offset):
                    self.cursor.fill((255, 0, 0))
                    screen.blit(self.cursor, self.pos)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_F3]:
                    print(time.ctime())
            # DevTool End
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE: 
                        self.pause = not self.pause
            pygame.display.flip()

class Player:
    def __init__(self) -> None:
        self.test = True
        self.player = pygame.image.load("monkey.png")
        self.velocity = [0, 0] # X, Y
        self.speed = 10
        self.position = [0, 0]
        self.mask = pygame.mask.from_surface(self.player)
        self.topLeft = self.position
        self.topRight = [self.position[0] - 64, self.position[1]]
        self.bottomLeft = [self.position[0], self.position[1] - 128]
        self.bottomRight = [self.position[0] - 64, self.position[1] - 128]
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
            self.position[0] = 1080 - 64
        if self.position[1] <= 0:
            self.position[1] = 0
        if self.position[1] >= 720 - 128:
            self.position[1] = 720 - 128
    def hitbox(self):
        return self.mask.get_bounding_rects()[0].move(self.position)
    
class Menu:
    def __init__(self) -> None:
        self.menuBackground = pygame.image.load("menu.png")
    def open(self, screen, pause):
        if pause:
            screen.blit(self.menuBackground, (0, 0))

pygame.init()

x = 1080
y = 720

screen = pygame.display.set_mode((x, y))

main = Main(screen)
main.run()

pygame.quit()
