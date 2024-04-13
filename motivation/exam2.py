import pygame
import random
import time

pygame.init()
pygame.mixer.init()

# Écran
x = 800
y = 600
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Jeux du poisson")
pygame.mixer.music.load("main.mp3")
pygame.mixer.music.play(-1, 0.0)
bubbleSound = pygame.mixer.Sound("bubble.mp3")
easter_egg = pygame.mixer.Sound("easter-egg.mp3")

poisson = pygame.image.load("poisson.png")
poisson_rect = poisson.get_rect()

background = pygame.image.load("oceanbackground.png").convert()

# Position initiale du poisson
poisson_rect.topleft = (random.randint(1, 600), random.randint(1, 500))

# Score
score = 0

last_move_time = pygame.time.get_ticks()

deplacement_speed = 5000

clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 50)

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(poisson, poisson_rect)

    score_text = font.render(
        "Score: " + str(score), True, (255, 0, 0))
    screen.blit(score_text, (370, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if poisson_rect.collidepoint(event.pos):
                score += 1
                print("Score:", score)
                poisson_rect.topleft = (random.randint(
                    1, 600), random.randint(1, 500))
                deplacement_speed = max(600, 5000 - score * 100)
                pygame.mixer.Sound.play(bubbleSound)
                last_move_time = pygame.time.get_ticks()
                if score == 50:
                    pygame.mixer.Sound.play(easter_egg)
            else:
                gameOver = pygame.mixer.Sound("gameover.mp3")
                pygame.mixer.Sound.play(gameOver)
                time.sleep(1)
                exit()

    if pygame.time.get_ticks() - last_move_time >= deplacement_speed:
        poisson_rect.topleft = (random.randint(1, 600), random.randint(1, 500))
        last_move_time = pygame.time.get_ticks()

    pygame.display.flip()
    clock.tick(30)
pygame.quit()
