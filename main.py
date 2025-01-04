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


def main():
    snowman = Snowman(WIDTH // 2, HEIGHT // 2)

    running = True
    while running:
        screen.fill(LIGHT_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        snowman.move(keys)
        snowman.draw(screen)


        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()


