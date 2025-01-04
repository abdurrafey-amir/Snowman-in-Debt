import pygame
import random
from snowman import Snowman
from task import Task

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


