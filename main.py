import pygame
import Colors
import random
from River import *
from Window import *
from Raft import *
import Params


param_window = ParamWindow()
river = River()
raft = Raft()

def get_labels():
    labels = []
    for key in Params.params:
        down = params_limits[key + " down"]
        up = params_limits[key + " up"]
        label = "[" + str(down) + " : " + str(up) + "]"
        labels.append(label)
        print(label)
    return labels


def game_loop(sc, clock):
    running = True
    input_boxes = param_window.create_input_boxes()
    x, y = raft.start_x, raft.start_y
    labels = get_labels()
    while running:
        sc.fill(Colors.WHITE)
        river.draw_river(sc)
        x, y = raft.draw_raft(sc, x, y)
        param_window.draw_param_window(sc)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for box in input_boxes:
                box.handle_event(event, sc)
        for i in range(len(input_boxes)):
            input_boxes[i].update()
            input_boxes[i].draw_limits(sc, labels[i])

        for box in input_boxes:
            box.draw(sc)

        pygame.display.flip()
        clock.tick(FPS)


def main():
    pygame.init()   # запускаем pygame
    pygame.mixer.init()  # для звука
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Visualize")
    clock = pygame.time.Clock()
    running = True
    game_loop(sc, clock)


if __name__ == '__main__':
    main()

