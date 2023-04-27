from Window import *
from River import *
from Params import *

class Raft():
    river = River()
    raft_width = 150
    raft_height = 50
    ledge_width = 20
    ledge_height = 25
    start_x = river.river_corner_x + river.river_width/2 - raft_width/2
    start_y = HEIGHT/2 + raft_height/2

    def up_ledge_coord(self,x, y):
        l_x = x + params["raft width"] / 2 - params["ledge width"] / 2
        l_y = y - params["ledge height"]
        return l_x, l_y

    def down_ledge_coord(self, x, y):
        l_x = x + params["raft width"] / 2 - params["ledge width"] / 2
        l_y = y + params["raft height"]
        return l_x, l_y

    def count_coord_y(self, cur_x, cur_y):
        cur_y -= 5
        if cur_y == 0:
            cur_y = HEIGHT
        return cur_y

    def draw_raft(self, sc, x=start_x, y=start_y):
        x, y = self.river.river_corner_x + self.river.river_width/2 - params["raft width"]/2, self.count_coord_y(x, y)
        pygame.draw.rect(sc, Colors.BROWN, (x, y, params["raft width"], params["raft height"]))
        up_ledge_x, up_ledge_y = self.up_ledge_coord(x, y)
        down_ledge_x, down_ledge_y = self.down_ledge_coord(x, y)
        pygame.draw.rect(sc, Colors.BROWN, (up_ledge_x, up_ledge_y, params["ledge width"],params["ledge height"]))
        pygame.draw.rect(sc, Colors.BROWN, (down_ledge_x, down_ledge_y, params["ledge width"],params["ledge height"]))
        return x, y

    # def draw_raft(self, sc, x=start_x, y=start_y):
    #     x, y = x, self.count_coord_y(x, y)
    #     pygame.draw.rect(sc, Colors.BROWN, (x, y, self.raft_width, self.raft_height))
    #     up_ledge_x, up_ledge_y = self.up_ledge_coord(x, y)
    #     down_ledge_x, down_ledge_y = self.down_ledge_coord(x, y)
    #     pygame.draw.rect(sc, Colors.BROWN, (up_ledge_x, up_ledge_y, self.ledge_width, self.ledge_height))
    #     pygame.draw.rect(sc, Colors.BROWN, (down_ledge_x, down_ledge_y, self.ledge_width, self.ledge_height))
    #     return x, y


