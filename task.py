import pygame

LIGHT_BLUE = (135, 206, 235)

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