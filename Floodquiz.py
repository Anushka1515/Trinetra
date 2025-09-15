# import pygame
# import random

# pygame.init()

# # Screen
# screen_width, screen_height = 950, 900
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Flood Preparedness Shooter")

# # Fonts
# font = pygame.font.Font(None, 36)

# # Load images
# background_img = pygame.image.load("Data/background.png").convert()  # your background
# player_img = pygame.image.load("Data/spaceship.png").convert_alpha()
# bullet_img = pygame.image.load("Data/bullet.png").convert_alpha()

# # Scale spaceship and bullet
# player_img = pygame.transform.scale(player_img, (180, 150))  # smaller spaceship
# bullet_img = pygame.transform.scale(bullet_img, (80, 50))  # smaller bullet

# # Player
# player_x, player_y = 370, 500
# player_speed = 5

# # Bullet
# bullet_x, bullet_y = 0, player_y
# bullet_speed = 7
# bullet_state = "ready"

# # Question & options
# question = "Which is the safest action during a flood?"
# options = ["A: Climb to higher ground", "B: Swim across river", "C: Stay in basement", "D: Panic"]
# # Single row of options, longer boxes
# option_y = 150
# option_x_start = 50
# option_spacing = 220
# option_width = 200
# option_height = 50
# option_rects = [
#     pygame.Rect(option_x_start + i * option_spacing, option_y, option_width, option_height)
#     for i in range(4)
# ]

# # Score
# score = 0

# running = True
# while running:
#     # Draw background
#     screen.blit(background_img, (0, 0))

#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Keys
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and player_x > 0:
#         player_x -= player_speed
#     if keys[pygame.K_RIGHT] and player_x < screen_width - player_img.get_width():
#         player_x += player_speed
#     if keys[pygame.K_SPACE] and bullet_state == "ready":
#         bullet_x = player_x + player_img.get_width() // 2 - bullet_img.get_width() // 2
#         bullet_y = player_y
#         bullet_state = "fire"

#     # Bullet movement
#     if bullet_state == "fire":
#         screen.blit(bullet_img, (bullet_x, bullet_y))
#         bullet_y -= bullet_speed
#         # Check collision with options
#         for idx, rect in enumerate(option_rects):
#             if rect.collidepoint(bullet_x + bullet_img.get_width() // 2, bullet_y):
#                 print(f"You hit option {options[idx][0]}")  # replace with scoring logic
#                 score += 1
#                 bullet_state = "ready"
#                 bullet_y = player_y

#         if bullet_y < 0:
#             bullet_state = "ready"

#     # Draw player (spaceship)
#     screen.blit(player_img, (player_x, player_y))

#     # Draw options
#     for idx, rect in enumerate(option_rects):
#         pygame.draw.rect(screen, (200, 0, 0), rect, border_radius=8)
#         text_surf = font.render(options[idx], True, (255, 255, 255))
#         screen.blit(text_surf, (rect.x + 5, rect.y + 10))

#     # Draw question
#     question_surf = font.render(question, True, (255, 255, 255))
#     screen.blit(question_surf, (50, 50))

#     # Draw score
#     score_surf = font.render(f"Score: {score}", True, (255, 255, 0))
#     screen.blit(score_surf, (650, 20))

#     pygame.display.update()


import pygame
import random

pygame.init()

# Screen
screen_width, screen_height = 950, 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flood Preparedness Shooter")

# Fonts
font = pygame.font.Font(None, 36)

# Load images
background_img = pygame.image.load("Data/background.png").convert()
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

player_img = pygame.image.load("Data/spaceship.png").convert_alpha()
bullet_img = pygame.image.load("Data/bullet.png").convert_alpha()
asteroid_img = pygame.image.load("Data/asteroid.png").convert_alpha()  # asteroid for options

# Scale images
player_img = pygame.transform.scale(player_img, (80, 50))  # smaller spaceship
bullet_img = pygame.transform.scale(bullet_img, (20, 40))  # smaller bullet
asteroid_img = pygame.transform.scale(asteroid_img, (500, 300))  # option asteroid size

# Player
player_x, player_y = 370, 700
player_speed = 5

# Bullet
bullet_x, bullet_y = 0, player_y
bullet_speed = 7
bullet_state = "ready"

# Question & options
question = "Which is the safest action during a flood?"
options = ["A: Climb to higher ground", "B: Swim across river", "D: Panic"]

option_y = 150
option_x_start = 40
option_spacing = 250
option_rects = [
    pygame.Rect(option_x_start + i * option_spacing, option_y, asteroid_img.get_width(), asteroid_img.get_height())
    for i in range(3)
]

# Score
score = 0

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    dt = clock.tick(60) / 1000

    # Draw background
    screen.blit(background_img, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_img.get_width():
        player_x += player_speed
    if keys[pygame.K_SPACE] and bullet_state == "ready":
        bullet_x = player_x + player_img.get_width() // 2 - bullet_img.get_width() // 2
        bullet_y = player_y
        bullet_state = "fire"

    # Bullet movement
    if bullet_state == "fire":
        screen.blit(bullet_img, (bullet_x, bullet_y))
        bullet_y -= bullet_speed

        # Check collision with options
        for idx, rect in enumerate(option_rects):
            if rect.collidepoint(bullet_x + bullet_img.get_width() // 2, bullet_y):
                print(f"You hit option {options[idx][0]}")
                score += 1
                bullet_state = "ready"
                bullet_y = player_y

        if bullet_y < 0:
            bullet_state = "ready"

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw options as asteroids
    for idx, rect in enumerate(option_rects):
        screen.blit(asteroid_img, (rect.x, rect.y))
        text_surf = font.render(options[idx], True, (255, 255, 255))
        # center text on asteroid
        text_rect = text_surf.get_rect(center=(rect.x + rect.width // 2, rect.y + rect.height // 2))
        screen.blit(text_surf, text_rect)

    # Draw question
    question_surf = font.render(question, True, (255, 255, 255))
    screen.blit(question_surf, (50, 50))

    # Draw score
    score_surf = font.render(f"Score: {score}", True, (255, 255, 0))
    screen.blit(score_surf, (650, 20))

    pygame.display.update()





