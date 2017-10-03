#! /usr/bin/python3

import copy, sys, time
from constants import *

def manhattan_distance(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

def heuristic(level_map, player_on_pit):
    pits = []   # empty
    boxes = []    # unplaced
    player = None
    heur = 0
    max_dist = sys.maxsize

    for y in range(LEVEL_SIZE[1]):
        for x in range(LEVEL_SIZE[0]):
            if level_map[y][x] == '~':
                player = [y, x]
                if player_on_pit:
                    pits.append(player)
            elif level_map[y][x] == '+':
                pits.append([y, x])
            elif level_map[y][x] == '*':
                boxes.append([y, x])
            elif level_map[y][x] == '@':
                heur -= max_dist

    for b in boxes:
        for p in pits:
            heur += manhattan_distance(b, p)
        player_dist = manhattan_distance(b, player)
        if max_dist > player_dist:
            max_dist = player_dist

    return heur + max_dist

def a_star_algo(level_map):
    open_set = [[level_map, 0, "", False, 0]]
    closed_set = []
    current = None

    while open_set:
        current = open_set.pop(0)
        closed_set.append(current)

        success = True
        for line in current[0]:
            for x in line:
                if x in ('+', '*'):
                    success = False
                    break
            if not success:
                break
        if success:
            return current[2]

        future_moves = []
        player = None
        directions = {
                        'UP' : [-1, 0],
                        'DOWN' : [1, 0],
                        'LEFT' : [0, -1],
                        'RIGHT' : [0, 1],
                     }

        for y in range(LEVEL_SIZE[1]):
            for x in range(LEVEL_SIZE[0]):
                if current[0][y][x] == '~':
                    player = [y, x]

        for k, v in directions.items():
            position = [player[0] + v[0], player[1] + v[1]]
            if current[0][position[0]][position[1]] == '#':
                continue

            future = copy.deepcopy(current)
            future[0][position[0]][position[1]] = '~'
            if current[3]:
                future[0][player[0]][player[1]] = '+'
            else:
                future[0][player[0]][player[1]] = '_'

            if current[0][position[0]][position[1]] == '+':
                future[3] = True
            elif current[0][position[0]][position[1]] in ('*', '@'):
                pos_of_shifted = [position[0] + v[0], position[1] + v[1]]
                if current[0][position[0]][position[1]] == '@':
                    future[3] = True
                if current[0][pos_of_shifted[0]][pos_of_shifted[1]] == '_':
                    future[0][pos_of_shifted[0]][pos_of_shifted[1]] = '*'
                elif current[0][pos_of_shifted[0]][pos_of_shifted[1]] == '+':
                    future[0][pos_of_shifted[0]][pos_of_shifted[1]] = '@'
                else:
                    continue

            future[2] += k + " "
            future[4] += 1
            future[1] += heuristic(future[0], future[3]) + future[4]
            future_moves.append(future)

        while future_moves:
            if not (future_moves[0] in open_set or future_moves[0] in closed_set):
                broken = False
                for x in range(len(open_set)):
                    if future_moves[0][1] < open_set[x][1]:
                        open_set.insert(x, future_moves[0])
                        broken = True
                        break
                if not broken:
                    open_set.append(future_moves[0])
            future_moves.pop(0)

def main():
    level_counter = 1
    while level_counter <= MAX_LEVELS:
        level_map = []
        try:
            line_counter = 0
            with open(LEVEL_FILE + str(level_counter), 'r') as level_map_file:
                for level_line in level_map_file:
                    line = level_line.rstrip('\n')
                    level_map.append([])
                    for char_index in range(len(line)):
                        level_map[line_counter].append(line[char_index])
                    line_counter += 1
        except FileNotFoundError:
            print("Level " + level_counter + " does not exist!")
            sys.exit()

        start_time = time.time()
        print("LEVEL " + str(level_counter))
        print("List of moves -> " + a_star_algo(level_map))
        print("Time taken : " + str(time.time() - start_time) + "\n")
        level_counter += 1

if __name__ == '__main__':
    main()
