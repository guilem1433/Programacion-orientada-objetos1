import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
BULLET_SPEED = 7
ENEMY_SPEED = 2
ENEMY_BULLET_SPEED = 4

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Galaga")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = PLAYER_SPEED
        self.lives = 3
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = ENEMY_SPEED
        self.direction = 1  # 1 for right, -1 for left

    def update(self):
        self.rect.x += self.speed * self.direction
        # Change direction and move down when reaching the edge
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.direction *= -1
            self.rect.y += 20

        # Random chance to shoot
        if random.random() < 0.005:  # Adjust this value to control shooting frequency
            self.shoot()

    def shoot(self):
        enemy_bullet = EnemyBullet(self.rect.centerx, self.rect.bottom)
        all_sprites.add(enemy_bullet)
        enemy_bullets.add(enemy_bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 0))  # Yellow color
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed = ENEMY_BULLET_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create enemies
for row in range(4):
    for column in range(10):
        enemy = Enemy(column * 70 + 50, row * 50 + 50)
        all_sprites.add(enemy)
        enemies.add(enemy)

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            elif event.key == pygame.K_ESCAPE:
                running = False

    # Update
    all_sprites.update()

    # Check for bullet-enemy collisions
    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for hit in hits:
        player.score += 10

    # Check for enemy bullet-player collisions
    hits = pygame.sprite.spritecollide(player, enemy_bullets, True)
    if hits:
        player.lives -= 1
        if player.lives <= 0:
            running = False

    # Check for direct enemy-player collisions
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        player.lives -= 1
        if player.lives <= 0:
            running = False

    # Respawn enemies if all are destroyed
    if len(enemies) == 0:
        for row in range(4):
            for column in range(10):
                enemy = Enemy(column * 70 + 50, row * 50 + 50)
                all_sprites.add(enemy)
                enemies.add(enemy)

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Display score and lives
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {player.score}", True, WHITE)
    lives_text = font.render(f"Lives: {player.lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (SCREEN_WIDTH - 120, 10))

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Game over
pygame.quit()
sys.exit()