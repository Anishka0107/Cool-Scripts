#! /usr/bin/python3

import pygame, sys
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption(GAME_NAME)

    start_game = IMAGE_START_GAME.get_rect()
    start_game.centerx = SCREEN_SIZE[0]/2
    start_game.y = 27
    move_to_next = IMAGE_NEXT.get_rect()
    move_to_next.center = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)
    level_complete = IMAGE_LEVEL_COMPLETE.get_rect()
    level_complete.centerx = SCREEN_SIZE[0]/2
    level_complete.y = 56
    reset_info = IMAGE_RESET_INFO.get_rect()
    reset_info.centerx = SCREEN_SIZE[0]/2
    reset_info.y = 300
    screen.fill(BG_COLOR)
    screen.blit(IMAGE_START_GAME, start_game)
    screen.blit(IMAGE_NEXT, move_to_next)
    screen.blit(IMAGE_RESET_INFO, reset_info)
    pygame.display.update()
    clock.tick()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_program()
            elif event.type == pygame.KEYDOWN:
                done = True

    level_counter = 1
    while level_counter <= MAX_LEVELS:
        level_map = []
        player_pos = []

        try:
            line_counter = 0
            with open(LEVEL_FILE + str(level_counter), 'r') as level_map_file:         
                for level_line in level_map_file:
                    line = level_line.rstrip('\n')
                    level_map.append([])
                    for char_index in range(len(line)):
                        level_map[line_counter].append(line[char_index])
                    line_counter += 1

                for y in range(LEVEL_SIZE[1]):
                    for x in range(LEVEL_SIZE[0]):
                        if level_map[y][x] == '~':
                            player_pos = [y, x]
 
        except FileNotFoundError:
            print("Level " + level_counter + " does not exist!")
            exit_program()

        reset_level = False
        player_on_pit = False
        pygame.display.set_caption(GAME_NAME + " - Level " + str(level_counter))

        screen.fill(BG_COLOR)
        for y in range(LEVEL_SIZE[1]):
            for x in range(LEVEL_SIZE[0]):
                tile_rect = pygame.Rect((TILE_SIZE * x, TILE_SIZE * y, TILE_SIZE, TILE_SIZE))
                screen.blit(TILES[level_map[y][x]], tile_rect)
        pygame.display.update()
        clock.tick()
        
        while True:
            character_move = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_program()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        character_move = [-1, 0]
                        TILES['~'] = IMAGE_CHAR_UP
                    elif event.key == pygame.K_DOWN:
                        character_move = [1, 0]
                        TILES['~'] = IMAGE_CHAR_DOWN
                    elif event.key == pygame.K_LEFT:
                        character_move = [0, -1]
                        TILES['~'] = IMAGE_CHAR_LEFT
                    elif event.key == pygame.K_RIGHT:
                        character_move = [0, 1]
                        TILES['~'] = IMAGE_CHAR_RIGHT
                    elif event.key == pygame.K_r:
                        reset_level = True
                        break
            if reset_level:
                break

            if character_move != None:
                orig_player_pos = player_pos
                old_player_on_pit = player_on_pit
                new_pos = [player_pos[0] + character_move[0], player_pos[1] + character_move[1]]
                if new_pos[0] in range(LEVEL_SIZE[1]) and new_pos[1] in range(LEVEL_SIZE[0]):
                    if level_map[new_pos[0]][new_pos[1]] in ('*', '@'):
                        new_pos_box = [new_pos[0] + character_move[0], new_pos[1] + character_move[1]]
                        if new_pos_box[0] in range(LEVEL_SIZE[1]) and new_pos_box[1] in range(LEVEL_SIZE[0]):
                            if level_map[new_pos_box[0]][new_pos_box[1]] in ('_', '+'):
                                if level_map[new_pos_box[0]][new_pos_box[1]] == '_':
                                    level_map[new_pos_box[0]][new_pos_box[1]] = '*'
                                elif level_map[new_pos_box[0]][new_pos_box[1]] == '+':
                                    level_map[new_pos_box[0]][new_pos_box[1]] = '@'
                            
                                player_on_pit = (level_map[new_pos[0]][new_pos[1]] == '@')
                                level_map[new_pos[0]][new_pos[1]] = '~'
                                if old_player_on_pit:
                                    level_map[player_pos[0]][player_pos[1]] = '+'
                                else:
                                    level_map[player_pos[0]][player_pos[1]] = '_'
                                tile_rect = pygame.Rect((TILE_SIZE * new_pos_box[1], TILE_SIZE * new_pos_box[0], TILE_SIZE, TILE_SIZE))
                                screen.blit(TILES[level_map[new_pos_box[0]][new_pos_box[1]]], tile_rect)
                                tile_rect = pygame.Rect((TILE_SIZE * new_pos[1], TILE_SIZE * new_pos[0], TILE_SIZE, TILE_SIZE))
                                screen.blit(TILES[level_map[new_pos[0]][new_pos[1]]], tile_rect)
                                player_pos = new_pos

                    elif level_map[new_pos[0]][new_pos[1]] in ('+', '_'):
                        player_on_pit = (level_map[new_pos[0]][new_pos[1]] == '+')
                        level_map[new_pos[0]][new_pos[1]] = '~'
                        if old_player_on_pit:
                            level_map[player_pos[0]][player_pos[1]] = '+'
                        else:
                            level_map[player_pos[0]][player_pos[1]] = '_'
                        tile_rect = pygame.Rect((TILE_SIZE * new_pos[1], TILE_SIZE * new_pos[0], TILE_SIZE, TILE_SIZE))
                        screen.blit(TILES[level_map[new_pos[0]][new_pos[1]]], tile_rect)
                        player_pos = new_pos

                    tile_rect = pygame.Rect((TILE_SIZE * orig_player_pos[1], TILE_SIZE * orig_player_pos[0], TILE_SIZE, TILE_SIZE))
                    screen.blit(TILES[level_map[orig_player_pos[0]][orig_player_pos[1]]], tile_rect)
                    pygame.display.update()
                    clock.tick()

            level_passed = True
            for i in range(len(level_map)):
                for j in range(len(level_map[i])):
                    if level_map[i][j] == '*':
                        level_passed = False
                        i = len(level_map)
                        break
            if level_passed:
                level_counter += 1
                screen.blit(IMAGE_LEVEL_COMPLETE, level_complete)
                screen.blit(IMAGE_NEXT, move_to_next)
                screen.blit(IMAGE_RESET_INFO, reset_info)
                pygame.display.update()
                clock.tick()
                done = False
                while not done:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit_program()
                        elif event.type == pygame.KEYDOWN:
                            done = True
                break
    exit_program()

def exit_program():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
