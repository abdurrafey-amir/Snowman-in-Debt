import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600

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