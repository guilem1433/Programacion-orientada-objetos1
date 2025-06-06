import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SNAKE_SPEED = 10  # Controls game speed

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 100, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]  # Start in middle
        self.length = 1
        self.direction = (1, 0)  # Initial direction: right
        self.score = 0
        self.color = GREEN
        self.head_color = DARK_GREEN

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        # Get current head position
        current = self.get_head_position()
        # Get direction
        x, y = self.direction
        # Calculate new position
        new = ((current[0] + x) % GRID_WIDTH, (current[1] + y) % GRID_HEIGHT)

        # Check if snake runs into itself
        if new in self.positions[1:]:
            return True  # Game over

        # Move snake
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

        return False  # Game continues

    def reset(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.length = 1
        self.direction = (1, 0)
        self.score = 0

    def render(self):
        # Draw snake body
        for position in self.positions[1:]:
            rect = pygame.Rect(position[0] * GRID_SIZE, position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, self.color, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

        # Draw snake head
        head_rect = pygame.Rect(self.positions[0][0] * GRID_SIZE, self.positions[0][1] * GRID_SIZE, GRID_SIZE,
                                GRID_SIZE)
        pygame.draw.rect(screen, self.head_color, head_rect)
        pygame.draw.rect(screen, BLACK, head_rect, 1)


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self, snake_positions=None):
        if snake_positions is None:
            snake_positions = []

        # Find a position that's not occupied by the snake
        while True:
            self.position = (random.randint(0, GRID_WIDTH - 1),
                             random.randint(0, GRID_HEIGHT - 1))
            if self.position not in snake_positions:
                break

    def render(self):
        rect = pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, self.color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)


def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (SCREEN_WIDTH, y))


def main():
    snake = Snake()
    food = Food()
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_SPACE:
                        snake.reset()
                        food.randomize_position(snake.positions)
                        game_over = False
                else:
                    # Change direction based on key press
                    if event.key == pygame.K_UP and snake.direction != (0, 1):
                        snake.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                        snake.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                        snake.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                        snake.direction = (1, 0)

        if not game_over:
            # Update snake
            game_over = snake.update()

            # Check if snake ate food
            if snake.get_head_position() == food.position:
                snake.length += 1
                snake.score += 10
                food.randomize_position(snake.positions)

        # Draw everything
        screen.fill(BLACK)
        draw_grid()
        snake.render()
        food.render()

        # Display score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {snake.score}", True, WHITE)
        screen.blit(score_text, (5, 5))

        # Game over text
        if game_over:
            font = pygame.font.SysFont(None, 72)
            game_over_text = font.render("GAME OVER", True, RED)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 160, SCREEN_HEIGHT // 2 - 36))

            font = pygame.font.SysFont(None, 36)
            restart_text = font.render("Press SPACE to restart", True, WHITE)
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 + 40))

        pygame.display.flip()
        clock.tick(SNAKE_SPEED)


if __name__ == "__main__":
    main()