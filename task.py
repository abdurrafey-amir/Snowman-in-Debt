import pygame

LIGHT_BLUE = (135, 206, 235)
BLACK = (0, 0, 0)

snow = []

class Task():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.completed = False
           

    def draw(self, screen):
        for i in snow:
            print(i)
            pygame.draw.rect(i[0], i[1], i[2])

    def check_collision(self, snowman):
        # check if snowman is shoveling the area
        for i in snow:
            rect = pygame.Rect(i[2])
            if snowman.rect.colliderect(rect): # need to make snowman hitbox
                snow.remove(i)
                return 10
        return 0