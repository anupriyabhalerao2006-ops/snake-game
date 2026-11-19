
import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Snake Game")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 35)

# Snake body
snake = [(100, 100), (80, 100), (60, 100)]
direction = (BLOCK, 0)

# Food position
food = (
    random.randrange(0, WIDTH, BLOCK),
    random.randrange(0, HEIGHT, BLOCK)
)

score = 0
running = True
game_over = False

# Main game loop
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != (0, BLOCK):
                direction = (0, -BLOCK)

            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK):
                direction = (0, BLOCK)

            elif event.key == pygame.K_LEFT and direction != (BLOCK, 0):
                direction = (-BLOCK, 0)

            elif event.key == pygame.K_RIGHT and direction != (-BLOCK, 0):
                direction = (BLOCK, 0)

    if not game_over:

        head_x, head_y = snake[0]

        new_head = (
            head_x + direction[0],
            head_y + direction[1]
        )

        snake.insert(0, new_head)

        # Eat food
        if new_head == food:
            score += 1

            food = (
                random.randrange(0, WIDTH, BLOCK),
                random.randrange(0, HEIGHT, BLOCK)
            )
        else:
            snake.pop()

        # Wall collision
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            game_over = True

        # Snake collision
        if new_head in snake[1:]:
            game_over = True

    # Draw background
    screen.fill(BLACK)

    # Draw snake
    for part in snake:
        pygame.draw.rect(
            screen, GREEN,
            (part[0], part[1], BLOCK, BLOCK)
        )

    # Draw food
    pygame.draw.rect(
        screen, RED,
        (food[0], food[1], BLOCK, BLOCK)
    )

    # Display score
    score_text = font.render(
        f"Score: {score}", True, WHITE
    )
    screen.blit(score_text, (10, 10))

    # Game over message
    if game_over:
        over_text = font.render("GAME OVER!", True, RED)
        screen.blit(over_text, (220, 180))

    pygame.display.update()
    clock.tick(10)

pygame.quit()
