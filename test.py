import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
window_width = 800
window_height = 600

# Couleurs
black = (0, 0, 0)
white = (255, 255, 255)

# Création de la fenêtre
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong Game")

# Initialisation des raquettes et de la balle
player_width = 15
player_height = 100
player_x = 50
player_y = window_height // 2 - player_height // 2

opponent_width = 15
opponent_height = 100
opponent_x = window_width - 50 - opponent_width
opponent_y = window_height // 2 - opponent_height // 2

ball_width = 15
ball_x = window_width // 2 - ball_width // 2
ball_y = window_height // 2 - ball_width // 2
ball_speed_x = 1 * random.choice((1, -1))
ball_speed_y = 1 * random.choice((1, -1))

# Définition de la vitesse des raquettes
player_speed = 0

# Score
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Gérer les mouvements de la raquette
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -8
            if event.key == pygame.K_DOWN:
                player_speed = 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed = 0

    # Mouvement de la raquette du joueur
    player_y += player_speed
    if player_y < 0:
        player_y = 0
    if player_y > window_height - player_height:
        player_y = window_height - player_height

    # Mouvement de la balle
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Rebond sur les bords
    if ball_y <= 0 or ball_y >= window_height - ball_width:
        ball_speed_y = -ball_speed_y

    # Rebond sur les raquettes
    if (
        (ball_x < player_x + player_width)
        and (ball_x > player_x)
        and (player_y < ball_y + ball_width)
        and (player_y + player_height > ball_y)
    ) or (
        (ball_x + ball_width > opponent_x)
        and (ball_x + ball_width < opponent_x + opponent_width)
        and (opponent_y < ball_y + ball_width)
        and (opponent_y + opponent_height > ball_y)
    ):
        ball_speed_x = -ball_speed_x

    # Marquer des points
    if ball_x <= 0:
        opponent_score += 1
        ball_x = window_width // 2 - ball_width // 2
        ball_y = window_height // 2 - ball_width // 2
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))
    if ball_x >= window_width:
        player_score += 1
        ball_x = window_width // 2 - ball_width // 2
        ball_y = window_height // 2 - ball_width // 2
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))

    # Dessiner tout
    screen.fill(black)
    pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(
        screen, white, (opponent_x, opponent_y, opponent_width, opponent_height)
    )
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_width, ball_width))

    # Afficher le score
    player_text = font.render("Player: " + str(player_score), True, white)
    opponent_text = font.render("Opponent: " + str(opponent_score), True, white)
    screen.blit(player_text, (20, 20))
    screen.blit(opponent_text, (window_width - 220, 20))

    pygame.display.flip()

# Quitter Pygame
pygame.quit()
