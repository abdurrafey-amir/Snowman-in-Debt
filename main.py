import pygame
import random

# initialize
pygame.init()

 # screen dimentions
WIDTH, HEIGHT = 800, 600

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (135, 206, 235)

# screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snowman in Debt')

# clock
clock = pygame.time.Clock()
FPS = 60

class Snowman():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.debt = 100 # starting debt
        self.health = 100 # starting health

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), 30) # head
        pygame.draw.circle(screen, BLACK, (self.x - 10, self.y - 10), 5) # eye
        pygame.draw.circle(screen, BLACK, (self.x + 10, self.y - 10), 5) # eye
        pygame.draw.circle(screen, WHITE, (self.x, self.y + 40), 40) # body
        pygame.draw.circle(screen, WHITE, (self.x, self.y + 100), 50) # base

    def move(self, keys):
        if keys[pygame.K_UP] and self.y > 30:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - 150:
            self.y += self.speed
        if keys[pygame.K_LEFT] and self.x > 30:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - 30:
            self.x += self.speed

class Task():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.completed = False

    def draw(self, screen):
        if not self.completed:
            pygame.draw.rect(screen, LIGHT_BLUE, (self.x, self.y, self.width, self.height))

    def check_collision(self, snowman):
        # check if snowman is shoveling the area
        if (self.x < snowman.x < self.x + self.width) and (self.y < snowman.y < self.y + self.height):
            self.completed = True
            return 10 # reward
        return 0





def main():
    snowman = Snowman(WIDTH // 2, HEIGHT // 2)
    tasks = [Task(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for _ in range(5)]

    running = True
    while running:
        screen.fill(LIGHT_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        snowman.move(keys)
        snowman.draw(screen)

        # draw tasks
        for task in tasks:
            task.draw(screen)
            reward = task.check_collision(snowman)
            if reward > 0:
                snowman.debt -= reward

        
        # display debt and health
        font = pygame.font.SysFont('Arial', 24)
        debt_text = font.render(f'Debt: ${snowman.debt}', True, BLACK)
        health_text = font.render(f'Health: {snowman.health}%', True, BLACK)
        screen.blit(debt_text, (10, 10))
        screen.blit(health_text, (10, 40))


        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()


