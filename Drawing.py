import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

#Don't change anything above this line

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)

PURPLE = (128, 0, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)

#Fills in background
display_surface.fill(PURPLE)

#Draws a circle
CENTER1 = (300, 300)
RADIUS1 = 100
pygame.draw.circle(display_surface, BLUE, CENTER1, RADIUS1)

CENTER2 = (250, 220)
RADIUS2 = 40
pygame.draw.circle(display_surface, BLACK, CENTER2, RADIUS2)

CENTER2 = (250, 220)
RADIUS2 = 20
pygame.draw.circle(display_surface, WHITE, CENTER2, RADIUS2)

CENTER3 = (350, 220)
RADIUS3 = 40
pygame.draw.circle(display_surface, BLACK, CENTER3, RADIUS3)

CENTER3 = (350, 220)
RADIUS3 = 20
pygame.draw.circle(display_surface, WHITE, CENTER3, RADIUS3)

START = (200, 300)
END = (400, 300)
pygame.draw.line(display_surface, BLACK, START, END, 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()