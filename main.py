'''
main loop for the RNN network
'''
import random
import time
import pygame
import snake

from settings import BACKGROUND_COLOR,\
    PLAYER_COLOR,\
    APPLE_COLOR,\
    WINDOW_SIZE,\
    SQUARE_SIZE,\
    FPS,\
    Position


def get_random_location():
    new_x = round(random.randint(1, round(WINDOW_SIZE[0] / SQUARE_SIZE) - 1)) * SQUARE_SIZE
    new_y = round(random.randint(1, round(WINDOW_SIZE[1] / SQUARE_SIZE) - 1)) * SQUARE_SIZE
    return new_x, new_y


def draw_next_player_position(main_display, player):
    for block in player.positions:
        pygame.draw.rect(main_display, PLAYER_COLOR, [block.x, block.y, SQUARE_SIZE, SQUARE_SIZE])


def game_loop(main_display):
    player = snake.Snake(Position(SQUARE_SIZE, SQUARE_SIZE))
    clock = pygame.time.Clock()
    continue_game = True
    draw_next_player_position(main_display, player)
    apple_x, apple_y = get_random_location()

    while continue_game and player.is_alive:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continue_game = False

            if event.type == pygame.KEYDOWN:
                player.update_direction(event.key)
                break

        if player.is_colliding(apple_x, apple_y):
            apple_x, apple_y = get_random_location()
            

        main_display.fill(BACKGROUND_COLOR)
        pygame.draw.rect(main_display, APPLE_COLOR, [apple_x, apple_y, SQUARE_SIZE, SQUARE_SIZE])
        player.move()
        draw_next_player_position(main_display, player)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

    print("Score: {}".format(len(player.positions)))

def main():
    pygame.init()
    main_display = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Snake RNN")
    main_display.fill(BACKGROUND_COLOR)
    game_loop(main_display)
 

if __name__ == "__main__":
    main()
