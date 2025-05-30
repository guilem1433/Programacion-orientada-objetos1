import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FROG_SIZE = 40
FROG_SPEED = 20
CAR_SPEED_MIN = 3
CAR_SPEED_MAX = 7
LOG_SPEED_MIN = 1
LOG_SPEED_MAX = 4
CAR_HEIGHT = 40
CAR_WIDTH = 80
LOG_HEIGHT = 40  # Reduced log height to make jumping easier
LOG_WIDTH = 120
LANE_HEIGHT = 60
WATER_TOP = 120
WATER_BOTTOM = WATER_TOP + 3 * LANE_HEIGHT
GOAL_TOP = 60
MOVEMENT_DELAY = 10  # Frames to wait between movements when key is held
JUMP_DISTANCE = 60  # Distance the frog jumps (matching lane height)

# Colors
GREEN = (10, 180, 10)
BROWN = (150, 75, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WATER_BLUE = (0, 100, 255)
GOAL_GREEN = (0, 200, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()


class Frog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((FROG_SIZE, FROG_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = FROG_SPEED
        self.lives = 3
        self.score = 0
        self.on_log = None
        self.movement_cooldown = 0
        self.jumping = False
        self.jump_start_pos = None
        self.jump_target_pos = None
        self.jump_progress = 0
        self.jump_speed = 0.1  # Controls jump animation speed

    # In the Frog class update method, fill in the missing code
    def update(self):
        # Handle jumping animation if in progress
        if self.jumping:
            self.jump_progress += self.jump_speed
            if self.jump_progress >= 1:
                # Jump completed
                self.rect.center = self.jump_target_pos
                self.jumping = False
                self.jump_progress = 0

                # Check if we landed on a log after jumping
                if WATER_TOP < self.rect.centery < WATER_BOTTOM:
                    log_hits = pygame.sprite.spritecollide(self, logs, False)
                    if log_hits:
                        self.on_log = log_hits[0]
                    else:
                        # Landed in water without a log
                        self.reset_position()
                        self.lives -= 1
            else:
                # Calculate position during jump (parabolic arc)
                t = self.jump_progress
                # Linear interpolation for x position
                new_x = self.jump_start_pos[0] + t * (self.jump_target_pos[0] - self.jump_start_pos[0])
                # Parabolic interpolation for y position (up then down)
                jump_height = 20  # Maximum height of jump above trajectory line
                new_y = self.jump_start_pos[1] + t * (self.jump_target_pos[1] - self.jump_start_pos[1])
                new_y -= jump_height * 4 * t * (1 - t)  # Parabolic formula
                self.rect.center = (new_x, new_y)
        else:
            # Handle continuous movement when keys are held down
            keys = pygame.key.get_pressed()

            # Decrease cooldown counter
            if self.movement_cooldown > 0:
                self.movement_cooldown -= 1

            # Move frog based on key presses if cooldown is zero
            if self.movement_cooldown == 0:
                moved = False
                if keys[pygame.K_UP]:
                    self.jump(0, -1)
                    moved = True
                elif keys[pygame.K_DOWN]:
                    self.jump(0, 1)
                    moved = True
                elif keys[pygame.K_LEFT]:
                    self.jump(-1, 0)
                    moved = True
                elif keys[pygame.K_RIGHT]:
                    self.jump(1, 0)
                    moved = True

                # If a movement key was pressed, reset the cooldown
                if moved:
                    self.movement_cooldown = MOVEMENT_DELAY
                    self.on_log = None  # Detach from log when jumping

        # Move with log if on one and not jumping
        if self.on_log and not self.jumping:
            self.rect.x += self.on_log.speed

        # Keep frog on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < GOAL_TOP:
            self.rect.top = GOAL_TOP
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        # Check if in water without a log and not jumping
        if WATER_TOP < self.rect.centery < WATER_BOTTOM and not self.on_log and not self.jumping:
            self.reset_position()
            self.lives -= 1

    def jump(self, dx, dy):
        # Start a jump with animation
        self.jumping = True
        self.jump_start_pos = self.rect.center

        # Calculate target position based on direction and JUMP_DISTANCE
        target_x = self.rect.centerx + dx * JUMP_DISTANCE
        target_y = self.rect.centery + dy * JUMP_DISTANCE
        self.jump_target_pos = (target_x, target_y)
        self.jump_progress = 0

    def move(self, dx, dy):
        # Legacy method, now uses jump
        self.jump(dx, dy)

    def reset_position(self):
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.on_log = None
        self.jumping = False


class Car(pygame.sprite.Sprite):
    def __init__(self, lane):
        super().__init__()
        self.image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.lane = lane
        self.speed = random.randint(CAR_SPEED_MIN, CAR_SPEED_MAX)

        # Set direction based on lane (alternating)
        self.direction = 1 if lane % 2 == 0 else -1
        self.speed *= self.direction

        # Set starting position
        if self.direction > 0:
            self.rect.right = 0
        else:
            self.rect.left = SCREEN_WIDTH

        # Set y position based on lane
        self.rect.y = SCREEN_HEIGHT - (lane + 1) * LANE_HEIGHT

    def update(self):
        self.rect.x += self.speed

        # Wrap around when off screen
        if (self.direction > 0 and self.rect.left > SCREEN_WIDTH) or \
                (self.direction < 0 and self.rect.right < 0):
            self.kill()


class Log(pygame.sprite.Sprite):
    def __init__(self, lane):
        super().__init__()
        self.image = pygame.Surface((LOG_WIDTH, LOG_HEIGHT))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.lane = lane

        # Set direction based on lane (alternating)
        self.direction = 1 if lane % 2 == 0 else -1
        self.speed = random.randint(LOG_SPEED_MIN, LOG_SPEED_MAX) * self.direction

        # Set starting position
        if self.direction > 0:
            self.rect.left = -LOG_WIDTH  # Start fully off-screen
        else:
            self.rect.right = SCREEN_WIDTH + LOG_WIDTH  # Start fully off-screen

        # Set y position based on lane
        self.rect.y = WATER_TOP + lane * LANE_HEIGHT + (LANE_HEIGHT - LOG_HEIGHT) // 2  # Center log in lane

    def update(self):
        self.rect.x += self.speed

        # Wrap around when off screen with buffer to prevent immediate reappearance
        if (self.direction > 0 and self.rect.left > SCREEN_WIDTH + 100) or \
                (self.direction < 0 and self.rect.right < -100):
            self.kill()


class Goal(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.Surface((FROG_SIZE * 1.5, FROG_SIZE))
        self.image.fill(GOAL_GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = GOAL_TOP
        self.filled = False

    def fill(self):
        if not self.filled:
            self.filled = True
            self.image.fill(YELLOW)
            return True
        return False


# Create sprite groups
all_sprites = pygame.sprite.Group()
cars = pygame.sprite.Group()
logs = pygame.sprite.Group()
goals = pygame.sprite.Group()

# Create frog
frog = Frog()
all_sprites.add(frog)

# Create goals
goal_width = FROG_SIZE * 1.5
goal_spacing = (SCREEN_WIDTH - 5 * goal_width) / 6
for i in range(5):
    x = goal_spacing + i * (goal_width + goal_spacing)
    goal = Goal(x)
    goals.add(goal)
    all_sprites.add(goal)

# Game variables
score = 0
level = 1
car_spawn_timer = 0
log_spawn_timer = 0
car_spawn_interval = 50
log_spawn_interval = 70

# Game loop
running = True
while running and frog.lives > 0:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Spawn cars
    car_spawn_timer += 1
    if car_spawn_timer >= car_spawn_interval:
        car_spawn_timer = 0
        lane = random.randint(0, 3)  # 4 lanes for cars
        car = Car(lane)
        cars.add(car)
        all_sprites.add(car)

    # Spawn logs
    log_spawn_timer += 0.8
    if log_spawn_timer >= log_spawn_interval:
        log_spawn_timer = 0
        lane = random.randint(0, 2)  # 3 lanes for logs
        log = Log(lane)
        logs.add(log)
        all_sprites.add(log)

    # Update
    all_sprites.update()

    # Check for car-frog collisions (only if not jumping)
    if not frog.jumping and pygame.sprite.spritecollide(frog, cars, False):
        frog.lives -= 1
        frog.reset_position()

    # Check for log-frog collisions (only if not jumping and in water)
    frog_in_water = WATER_TOP < frog.rect.centery < WATER_BOTTOM
    if frog_in_water and not frog.jumping:
        log_hits = pygame.sprite.spritecollide(frog, logs, False)
        if log_hits:
            frog.on_log = log_hits[0]
        elif not frog.on_log:  # Only reset if not already on a log
            frog.reset_position()
            frog.lives -= 1
    elif not frog_in_water and not frog.jumping:
        # Not in water, so not on a log
        frog.on_log = None

    # Check for goal collisions
    goal_hits = pygame.sprite.spritecollide(frog, goals, False)
    if goal_hits and not frog.jumping:
        if goal_hits[0].fill():
            frog.score += 100
            frog.reset_position()

            # Check if all goals are filled
            all_filled = all(goal.filled for goal in goals)
            if all_filled:
                # Reset goals and increase difficulty
                for goal in goals:
                    goal.filled = False
                    goal.image.fill(GOAL_GREEN)
                level += 1
                car_spawn_interval = max(20, car_spawn_interval - 5)
                log_spawn_interval = max(40, log_spawn_interval - 5)
                frog.score += 500
        else:
            # Already filled goal
            frog.reset_position()


    # Instead of just drawing all sprites at once, draw them in layers
    def draw_game():
        # Draw background
        screen.fill(BLACK)

        # Draw water
        pygame.draw.rect(screen, WATER_BLUE, (0, WATER_TOP, SCREEN_WIDTH, WATER_BOTTOM - WATER_TOP))

        # Draw goal area
        pygame.draw.rect(screen, (100, 100, 100), (0, GOAL_TOP, SCREEN_WIDTH, GOAL_TOP + FROG_SIZE))

        # Draw sprites in layers - background objects first, then frog on top
        for entity in all_sprites:
            if entity != frog:  # Draw everything except frog
                screen.blit(entity.image, entity.rect)

        # Draw frog last so it's on top of everything
        screen.blit(frog.image, frog.rect)

        # Display score, lives and level
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {frog.score}", True, WHITE)
        lives_text = font.render(f"Lives: {frog.lives}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (SCREEN_WIDTH - 120, 10))
        screen.blit(level_text, (SCREEN_WIDTH // 2 - 50, 10))


    # In the game loop, replace the drawing section with a call to this function
    # ...
    # Update
    all_sprites.update()

    # Check collisions
    # ...

    # Draw
    draw_game()

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Game over
if frog.lives <= 0:
    font = pygame.font.SysFont(None, 72)
    game_over_text = font.render("GAME OVER", True, RED)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 36))
    pygame.display.flip()
    pygame.time.wait(2000)

pygame.quit()
sys.exit()