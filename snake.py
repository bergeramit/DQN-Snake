'''
The Snake that plays the snake game
'''
import pygame
from settings import SQUARE_SIZE, WINDOW_SIZE, Position
from collections import deque

class Snake:

    DIRECTIONS = {
        pygame.K_LEFT: (-SQUARE_SIZE, 0),
        pygame.K_RIGHT: (SQUARE_SIZE, 0),
        pygame.K_UP: (0, -SQUARE_SIZE),
        pygame.K_DOWN: (0, SQUARE_SIZE)
    }

    HORIZONTAL_KEYS = [pygame.K_LEFT, pygame.K_RIGHT]
    VERTICAL_KEYS = [pygame.K_UP, pygame.K_DOWN]

    def __init__(self, starting_position):
        self.head = starting_position
        self.positions = deque()
        self.positions.append(starting_position)
        self.time_to_grow = 0
        self.should_grow = False
        self.is_alive = True

        self.x_direction, self.y_direction = (SQUARE_SIZE, 0)
        self.direction = pygame.K_RIGHT


    def is_move_illegal(self, new_direction):
        illigal_horizontal_move = (new_direction in Snake.HORIZONTAL_KEYS) and \
            (self.direction in Snake.HORIZONTAL_KEYS)

        illigal_vertical_move = (new_direction in Snake.VERTICAL_KEYS) and \
            (self.direction in Snake.VERTICAL_KEYS)

        return illigal_horizontal_move or illigal_vertical_move


    def update_direction(self, new_direction):
        if self.is_move_illegal(new_direction):
            
            # Ignoring illigal moves
            return

        self.direction = new_direction
        self.x_direction, self.y_direction = Snake.DIRECTIONS[new_direction]


    def inside_border(self):
        return ((0 <= self.head.x < WINDOW_SIZE[0]) and (0 <= self.head.y < WINDOW_SIZE[1]))

    def update_size(self):
        if self.time_to_grow == 0 and self.should_grow:
            # Do not pop last element in order to grow the snake
            self.should_grow = False

        else:
            self.time_to_grow = (self.time_to_grow - 1) if self.should_grow else 0
            self.positions.popleft()

    def move(self):
        self.update_size()
        next_position = Position(self.head.x + self.x_direction, self.head.y + self.y_direction)
        
        if next_position in self.positions or not self.inside_border():
            self.is_alive = False
        
        self.head = next_position
        self.positions.append(next_position)


    def is_colliding(self, object_x, object_y):
        if object_x == self.head.x and object_y == self.head.y:
            self.time_to_grow = len(self.positions)
            self.should_grow = True
            return True

        return False
