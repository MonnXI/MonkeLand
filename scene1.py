import pygame


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(0, 471)
        self.area = pygame.Rect(0, 600, 1080, 120)
        self.area_color = "red"
        self.life = 0
        self.energy = 0
        self.alive = True
        self.power_up = Banana_Energy(100, 536)
        self.coconut = Power_Up_Life(500, 536)
        self.plateform = Platform(100, 150)

    def heart(self):
        if self.life == 0:
            self.screen.blit(heart0, (5, 4))
        elif self.life == 1:
            self.screen.blit(heart1, (5, 4))
        elif self.life == 2:
            self.screen.blit(heart2, (5, 4))
        elif self.life == 3:
            self.screen.blit(heart3, (5, 4))
        elif self.life == 4:
            self.screen.blit(heart4, (5, 4))
        elif self.life == 5:
            self.screen.blit(heart5, (5, 4))
        elif self.life == 6:
            self.screen.blit(heart6, (5, 4))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            self.life += 1

    def bananapeel(self):
        if self.energy == 0:
            self.screen.blit(peel0, (1016, 0))
        elif self.energy == 1:
            self.screen.blit(peel1, (1016, 4))
        elif self.energy == 2:
            self.screen.blit(peel2, (1016, 0))
        elif self.energy == 3:
            self.screen.blit(peel3, (1016, 0))
        elif self.energy == 4:
            self.screen.blit(peel4, (1016, 0))
        elif self.energy == 5:
            self.screen.blit(peel5, (1016, 0))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            self.energy += 1

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
# Axe X
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.player.velocity[0] = -1
        elif pressed[pygame.K_RIGHT]:
            self.player.velocity[0] = 1
        else:
            self.player.velocity[0] = 0
# Axe Y
        if pressed[pygame.K_UP]:
            self.player.velocity[1] = -1
        elif pressed[pygame.K_DOWN]:
            self.player.velocity[1] = 1
        else:
            self.player.velocity[1] = 0.7

    def display(self):
        self.screen.fill(pygame.Color("white"))
        self.player.draw(self.screen)
        if self.power_up.show:
            self.power_up.draw(self.screen)
        if self.coconut.show:
            self.coconut.draw(self.screen)
        if self.plateform.show:
            self.plateform.draw(self.screen)
        self.screen.blit(grasspng, (0, 600))
        self.screen.blit(grasspng, (128, 600))
        self.screen.blit(grasspng, (256, 600))
        self.screen.blit(grasspng, (384, 600))
        self.screen.blit(grasspng, (512, 600))
        self.screen.blit(grasspng, (640, 600))
        self.screen.blit(grasspng, (768, 600))
        self.screen.blit(grasspng, (896, 600))
        self.screen.blit(grasspng, (1024, 600))
        self.heart()
        self.bananapeel()
        pygame.display.flip()

    def update(self):
        self.player.move()
        if self.area.colliderect(self.player.rect):
            self.player.reset_position(471)
        if self.player.rect.colliderect(self.power_up.rect):
            if self.power_up.show:
                self.energy -= 1
                self.power_up.show = False
        if self.player.rect.colliderect(self.coconut.rect):
            if self.coconut.show:
                self.life -= 1
                self.coconut.show = False
        if self.life == -1:
            self.life = 0
        if self.energy == -1:
            self.energy = 0
        if self.energy == 6:
            self.energy = 5

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)
            if self.life == 6:
                self.alive = False
            if self.alive == False:
                self.running = False


class Banana_Energy:
    def __init__(self, posx, posy):
        self.power_up = pygame.image.load("banana.png")
        self.banana = self.power_up
        self.rect = self.banana.get_rect(x=posx, y=posy)
        self.show = True

    def draw(self, screen):
        if self.show:
            screen.blit(self.banana, self.rect)


class Power_Up_Life:
    def __init__(self, posx, posy):
        self.power_up = pygame.image.load("coconut.png")
        self.coconut = self.power_up
        self.rect = self.coconut.get_rect(x=posx, y=posy)
        self.show = True

    def draw(self, screen):
        if self.show:
            screen.blit(self.coconut, self.rect)


class Platform:
    def __init__(self, posy, posx):
        self.platform = pygame.image.load("plateform.png")
        self.rect = self.platform.get_rect(x=posx, y=posy)
        self.show = True

    def draw(self, screen):
        if self.show:
            screen.blit(self.platform, self.rect)


class Player:
    def __init__(self, posx, posy):
        self.monkeyplayer = pygame.image.load("monkey.png")
        self.image = self.monkeyplayer
        self.rect = self.image.get_rect(x=posx, y=posy)
        self.speed = 5
        self.velocity = [0, 0.7]

    def reset_position(self, reset_pos):
        self.rect.y = reset_pos

    def move(self):
        self.rect.move_ip(
            self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


pygame.init()

x = 1080
y = 720

screen = pygame.display.set_mode((x, y))
grasspng = pygame.image.load("grass.png")
heart0 = pygame.image.load("heart-0.png")
heart1 = pygame.image.load("heart-1.png")
heart2 = pygame.image.load("heart-2.png")
heart3 = pygame.image.load("heart-3.png")
heart4 = pygame.image.load("heart-4.png")
heart5 = pygame.image.load("heart-5.png")
heart6 = pygame.image.load("heart-6.png")
peel0 = pygame.image.load("bananapeel-0.png")
peel1 = pygame.image.load("bananapeel-1.png")
peel2 = pygame.image.load("bananapeel-2.png")
peel3 = pygame.image.load("bananapeel-3.png")
peel4 = pygame.image.load("bananapeel-4.png")
peel5 = pygame.image.load("bananapeel-5.png")
game_instance = Game(screen)
game_instance.run()

pygame.quit()
