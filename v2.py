import pygame
import time

class Main:
    def __init__(self, screen):
        self.running = True
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.devTool = False
    def devTools(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_F1]:
            self.devTool = True
        if pressed[pygame.K_F2]:
            self.devTool = False
    def run(self):
        devTool = self.devTools()
        while self.running:
            screen.fill((0,0,0))
            self.devTools()
            if self.devTool:
                mousex, mousey = pygame.mouse.get_pos()
                font = pygame.font.Font(None, 46)
                mousePos = font.render(f'{mousex}, {mousey}', True, (255, 255, 255))
                screen.blit(mousePos, (25, 25))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
            self.clock.tick(30)

class Player:
    def __init__(self) -> None:
        pass



pygame.init()

x = 1080
y = 720

screen = pygame.display.set_mode((x, y))

main = Main(screen)
main.run()

pygame.quit()
