import pygame

# initializes pygame
pygame.init()

# ----------------
#    CONSTANTS
# ----------------

width = 600
height = 600
line_width = 15
board_rows = 3
board_cols = 3
circle_radius = 60
circle_width = 15
cross_width = 25
space = 55

red = (255, 0, 0)
bg_color = (28, 170, 156)
line_color = (23, 145, 135)
circle_color = (239, 231, 200)
cross_color = (66, 66, 66)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('MAG')
screen.fill(bg_color)
