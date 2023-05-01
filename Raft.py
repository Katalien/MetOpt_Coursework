import pygame

import Colors
from Window import *
from River import *
from Params import *
import Window


class Raft():
    river = River()
    raft_width = 150
    raft_height = 50
    ledge_width = 20
    ledge_height = 25
    start_x = river.river_corner_x + river.river_width/2 - raft_width/2
    start_y = raft_height/2

    def up_ledge_center_coord(self,x, y):
        l_x = x - params["raft width"] / 2 + params["dist from left"] + params["ledge width"]/2
        l_y = y - params["raft height"]/2 - params["ledge height"]/2
        return l_x, l_y

    def down_ledge_coord(self, x, y):
        l_x = x - params["raft width"] / 2 + params["dist from left"] + params["ledge width"]/2
        l_y = y + params["raft height"]/2 + params["ledge height"]/2 - 1
        return l_x, l_y

    def count_coord_y(self, cur_x, cur_y):
        cur_y -= 5
        if cur_y == 0:
            cur_y = HEIGHT
        return cur_y

    def count_coordinates(self, x, y, angle):
        if y > constant_params["river width"] - 3:
            angle = 0
            y -= 5
        elif y > constant_params["river width"]/2:
            angle += 5
            x += 5
            y -=5
        else:
            x += 5
        if x > Window.WIDTH:
           x, y = River.river_corner_x + constant_params["river width"]/2, HEIGHT
           angle = 0
        return x, y, angle
    def rotate(self, surface, angle, pivot, offset):
        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
        rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
        # Add the offset vector to the center/pivot point to shift the rect.
        rect = rotated_image.get_rect(center=pivot + rotated_offset)
        return rotated_image, rect  # Return the rotated image and shifted rect.

    def draw_raft(self, sc, x=start_x, y=start_y, angle=0):
        # x, y = x, self.count_coord_y(x, y)
        x, y, angle = self.count_coordinates(x, y, angle)
        rect_surf = pygame.Surface((params["raft width"], params["raft height"]), pygame.SRCALPHA)
        rect_surf.fill(Colors.BROWN)
        # rect_surf.set_colorkey(Colors.BLACK)
        pivot = [x, y]
        offset = pygame.math.Vector2(0, 0)
        rotated_image, rect = self.rotate(rect_surf, angle, pivot, offset)
        sc.blit(rotated_image, rect)

        up_ledge_x, up_ledge_y = self.up_ledge_center_coord(x, y)
        down_ledge_x, down_ledge_y = self.down_ledge_coord(x, y)
        up_surf = pygame.Surface((params["ledge width"], params["ledge height"]), pygame.SRCALPHA)
        up_surf.fill(Colors.BROWN)
        up_pivot = [x, y]
        up_offset = pygame.math.Vector2(-params["raft width"]/2 + params["dist from left"] + params["ledge width"]/2, -params["raft height"]/2 - params["ledge height"]/2)
        up_rotated_image, up_rect = self.rotate(up_surf, angle, up_pivot, up_offset)
        sc.blit(up_rotated_image, up_rect)



        down_surf = pygame.Surface((params["ledge width"], params["ledge height"]), pygame.SRCALPHA)
        down_surf.fill(Colors.BROWN)
        down_pivot = [x, y]
        down_offset = pygame.math.Vector2(
            -params["raft width"] / 2 + params["dist from left"] + params["ledge width"] / 2,
            params["raft height"] / 2 + params["ledge height"] / 2)
        down_rotated_image, down_rect = self.rotate(down_surf, angle, down_pivot, down_offset)
        sc.blit(down_rotated_image, down_rect)


        # rect = pygame.draw.rect(sc, Colors.BROWN, (x, y, params["raft width"], params["raft height"]))
        # up_ledge_x, up_ledge_y = self.up_ledge_coord(x, y)
        # down_ledge_x, down_ledge_y = self.down_ledge_coord(x, y)
        # pygame.draw.rect(sc, Colors.BROWN, (up_ledge_x, up_ledge_y, params["ledge width"],params["ledge height"]))
        # pygame.draw.rect(sc, Colors.BROWN, (down_ledge_x, down_ledge_y, params["ledge width"],params["ledge height"]))
        return x, y, angle

    # def draw_raft(self, sc, x=start_x, y=start_y):
    #     x, y = x, self.count_coord_y(x, y)
    #     pygame.draw.rect(sc, Colors.BROWN, (x, y, self.raft_width, self.raft_height))
    #     up_ledge_x, up_ledge_y = self.up_ledge_coord(x, y)
    #     down_ledge_x, down_ledge_y = self.down_ledge_coord(x, y)
    #     pygame.draw.rect(sc, Colors.BROWN, (up_ledge_x, up_ledge_y, self.ledge_width, self.ledge_height))
    #     pygame.draw.rect(sc, Colors.BROWN, (down_ledge_x, down_ledge_y, self.ledge_width, self.ledge_height))
    #     return x, y


