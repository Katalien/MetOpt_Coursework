# # pygame.transform module
# # https://www.pygame.org/docs/ref/transform.html
# #
# # How do I rotate an image around its center using PyGame?
# # https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame/54714144#54714144
# #
# # How to rotate an image around its center while its scale is getting larger(in Pygame)
# # https://stackoverflow.com/questions/54462645/how-to-rotate-an-image-around-its-center-while-its-scale-is-getting-largerin-py/54713639#54713639
# #
# # GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Circle and circle
# # https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_rotate.md
#
# import pygame
# import os
#
# # os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))
# pygame.init()
#
# screen = pygame.display.set_mode((300, 300))
# clock = pygame.time.Clock()
# try:
#     image = pygame.image.load('icon/AirPlaneFront1-128.png')
# except:
#     text = pygame.font.SysFont('Times New Roman', 50).render('image', False, (255, 255, 0))
#     image = pygame.Surface((text.get_width() + 1, text.get_height() + 1))
#     pygame.draw.rect(image, (0, 0, 255), (1, 1, *text.get_size()))
#     image.blit(text, (1, 1))
#
# start = False
# angle = 0
# done = False
# while not done:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
#             start = True
#
#     # pos = (screen.get_width() / 2, screen.get_height() / 2)
#     pos = (0, 100)
#
#     screen.fill(0)
#     rotated_image = pygame.transform.rotate(image, angle)
#     if start:
#         angle += 1
#
#     screen.blit(rotated_image, pos)
#     # pygame.draw.rect(screen, (255, 0, 0), (*pos, *rotated_image.get_size()), 2)
#
#     # pygame.draw.line(screen, (0, 255, 0), (pos[0] - 20, pos[1]), (pos[0] + 20, pos[1]), 3)
#     # pygame.draw.line(screen, (0, 255, 0), (pos[0], pos[1] - 20), (pos[0], pos[1] + 20), 3)
#     # pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)
#
#     pygame.display.flip()
#
# pygame.quit()
# exit()

import pygame as pg
import Colors

def rotate(surface, angle, pivot, offset):
    rotated_image = pg.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.


pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
BG_COLOR = pg.Color('gray12')
# The original image will never be modified.
IMAGE = pg.Surface((140, 60), pg.SRCALPHA)
pg.draw.polygon(IMAGE, pg.Color('dodgerblue3'), ((0, 0), (140, 30), (0, 60)))

# Store the original center position of the surface.
pivot = [200, 250]
# This offset vector will be added to the pivot point, so the
# resulting rect will be blitted at `rect.topleft + offset`.
offset = pg.math.Vector2(100, 0)
angle = 0

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        angle += 1
    elif keys[pg.K_a] or keys[pg.K_LEFT]:
        angle -= 1
    if keys[pg.K_f]:
        pivot[0] += 2

    # Rotated version of the image and the shifted rect.
    rotated_image, rect = rotate(IMAGE, angle, pivot, offset)

    # Drawing.
    screen.fill(Colors.GREY)
    screen.blit(rotated_image, rect)  # Blit the rotated image.
    pg.draw.circle(screen, (30, 250, 70), pivot, 3)  # Pivot point.
    # pg.draw.rect(screen, (30, 250, 70), rect, 1)  # The rect.
    # pg.display.set_caption('Angle: {}'.format(angle))
    pg.display.flip()
    clock.tick(30)

pg.quit()