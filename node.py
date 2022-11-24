import pygame
from typing import NamedTuple


class GridLocation(NamedTuple):

    row: int
    col: int


class Node:

    COLORS = {'white': (255, 255, 255), 'black': (0, 0, 0), 'green': (0, 255, 0),
              'red': (255, 0, 0), 'purple': (127, 255, 212), 'blue': (64, 224, 208),
              'yellow': (255, 255, 51)}

    PURPLE = ((230, 230, 250), (216, 191, 216), (221, 160, 221),
              (238, 130, 238), (218, 112, 214), (255, 0, 255),
              (255, 0, 255), (186, 85, 211), (147, 112, 219),
              (138, 43, 226), (148, 0, 211), (153, 50, 204),
              (139, 0, 139), (128, 0, 128), (75, 0, 130), (75, 0, 130),
              (75, 0, 130), (75, 0, 130), (75, 0, 130), (75, 0, 130))

    BLUE = [(224, 255, 255), (0, 255, 255), (0, 255, 255), (127, 255, 212),
            (102, 205, 170), (175, 238, 238), (64, 224, 208), (72, 209, 204),
            (0, 206, 209), (32, 178, 170), (95, 158, 160), (0, 139, 139),
            (0, 128, 128), (173, 216, 230), (135, 206, 250), (135, 206, 235),
            (0, 191, 255)]

    def __init__(self, state, parent, rect_dim,
                 heuristic=None, cost=None):
        self.state = state
        self.row, self.col = state.row, state.col
        self.__color = self.COLORS['white']
        self.color_name = 'white'

        self.rect_dim = rect_dim

        self.parent = parent
        self.cost = cost
        self.__heuristic = heuristic

        self.__animation_color = self.BLUE

        self.__animation_stages = len(self.__animation_color)
        self.__rect = False
        self.__stage = 0

    def __repr_(self):
        return repr(self.state)

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def draw_node(self, window):

        if self.color_name == 'white':
            self.__rect = False
            pygame.draw.rect(window, self.__color, pygame.Rect(self.col * self.rect_dim, self.row * self.rect_dim,
                                                               self.rect_dim, self.rect_dim))
        else:
            k = 1
            if self.color_name == 'purple':
                if self.__stage // k < self.__animation_stages:
                    color = self.__animation_color[self.__stage // k]
                else:
                    color = self.__animation_color[-1]

            else:
                color = self.__color
                self.__animation_stages = 10

            if not self.__rect:

                if self.__stage >= self.__animation_stages:
                    self.__rect = True
                    self.__stage = 0

                total_radius = self.rect_dim // 2
                radius = total_radius // self.__animation_stages * 2.5 * self.__stage

                if radius >= total_radius:
                    self.__rect = True
                    radius = total_radius

                pygame.draw.circle(window, color,
                                   (self.col * self.rect_dim + total_radius,
                                    self.row * self.rect_dim + total_radius),
                                   radius=radius)

                self.__stage += 1

            else:

                pygame.draw.rect(window, self.__color, pygame.Rect(self.col * self.rect_dim,
                                                                   self.row * self.rect_dim,
                                                                   self.rect_dim, self.rect_dim))

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        assert color in self.COLORS, f'{color} is not valid. Try one of {self.COLORS.keys()}'
        self.__color = self.COLORS[color]
        self.color_name = color

    @property
    def heuristic(self):
        return self.__heuristic

    @heuristic.setter
    def heuristic(self, value):
        self.__heuristic = value

    def __repr__(self):
        return f"Node({self.row}, {self.col}, {self.__color})"
