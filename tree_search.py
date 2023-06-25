# God's Algorithm for a 2x2 pocket cube
# By Sergio Lopez original version 5-23-2021, edited version 6-25-2023

# A cube will be represented by strings

# Corner 0 (Pivot): White-Red-Blue
# Corner 1 : White-Red-Green
# Corner 2: White-Green-Orange
# Corner 3: White-Orange-Blue
# Corner 4: Yellow-Blue-Red
# Corner 5: Yellow-Red-Green
# Corner 6: Yellow-Green-Orange
# Corner 7: Yellow-Orange-Blue

# Orientation 0: White/Yellow facing up/down
# Orientation 1: Low level left and top level right
# Orientation 2: Low level right and top level left

# Start with the 4 'down' and then go 'up', right direction

# For example, solved cube is '10203040506070'

import time
import random
import csv

class Cube:
    def __init__(self, scramble=None):
        if scramble is None:
            scramble = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]
        self.cube = scramble
        self.counter = 0
        self.moves = []
        self.steps = ''
        self.states = {'': self.cube}

    def cube_to_string(self):
        cube_string = ''
        for elem in self.cube:
            for num in elem:
                cube_string += str(num)
        cube_string = cube_string[2:]
        return cube_string

    def get_data_to_csv(self, n_depth):
        cube_list = []
        for corner in self.cube:
            for elem in corner:
                cube_list.append(elem)
        cube_list.append(n_depth)
        return cube_list

    def render(self):
        print(self.cube, self.counter)

    def move(self, move):
        self.counter += 1
        if move == 'r_normal':
            save = self.cube[1]
            self.cube[1] = [self.cube[2][0], (self.cube[2][1] + 1) % 3]
            self.cube[2] = [self.cube[6][0], (self.cube[6][1] + 2) % 3]
            self.cube[6] = [self.cube[5][0], (self.cube[5][1] + 1) % 3]
            self.cube[5] = [save[0], (save[1]+2) % 3]
        elif move == 'r_prime':
            save = self.cube[1]
            self.cube[1] = [self.cube[5][0], (self.cube[5][1] + 1) % 3]
            self.cube[5] = [self.cube[6][0], (self.cube[6][1] + 2) % 3]
            self.cube[6] = [self.cube[2][0], (self.cube[2][1] + 1) % 3]
            self.cube[2] = [save[0], (save[1] + 2) % 3]
        elif move == 'r_twice':
            save1 = self.cube[1]
            save2 = self.cube[2]
            self.cube[1] = self.cube[6]
            self.cube[2] = self.cube[5]
            self.cube[6] = save1
            self.cube[5] = save2
        elif move == 'u_normal':
            save = self.cube[4]
            self.cube[4] = self.cube[5]
            self.cube[5] = self.cube[6]
            self.cube[6] = self.cube[7]
            self.cube[7] = save
        elif move == 'u_prime':
            save = self.cube[4]
            self.cube[4] = self.cube[7]
            self.cube[7] = self.cube[6]
            self.cube[6] = self.cube[5]
            self.cube[5] = save
        elif move == 'u_twice':
            save4 = self.cube[4]
            save5 = self.cube[5]
            self.cube[4] = self.cube[6]
            self.cube[6] = save4
            self.cube[5] = self.cube[7]
            self.cube[7] = save5
        elif move == 'b_normal':  # Equal to u_normal
            save = self.cube[2]
            self.cube[2] = [self.cube[6][0], (self.cube[6][1] + 1) % 3]
            self.cube[6] = [self.cube[7][0], (self.cube[7][1] + 2) % 3]
            self.cube[7] = [self.cube[3][0], (self.cube[3][1] + 1) % 3]
            self.cube[3] = [save[0], (save[1] + 2) % 3]
        elif move == 'b_prime':
            save = self.cube[2]
            self.cube[2] = [self.cube[3][0], (self.cube[3][1] + 1) % 3]
            self.cube[3] = [self.cube[7][0], (self.cube[7][1] + 2) % 3]
            self.cube[7] = [self.cube[6][0], (self.cube[6][1] + 1) % 3]
            self.cube[6] = [save[0], (save[1] + 2) % 3]
        elif move == 'b_twice':
            save2 = self.cube[2]
            save3 = self.cube[3]
            self.cube[2] = self.cube[7]
            self.cube[7] = save2
            self.cube[3] = self.cube[6]
            self.cube[6] = save3


def intersection(dict1, dict2):
    move_sol = None
    for key1 in dict1:
        for key2 in dict2:
            if dict1[key1] == dict2[key2]:
                move_sol = key2+opposite_move(key1)
                # Comment line below to show all the god algorithms
                # Uncommented brings only one solution
                return move_sol
                # break
    if move_sol == None:
        return None
    # else: (Also uncomment this line to show all solutions)
    #     return inter

def opposite_move(moves):
    add_str = ''
    for char in moves:
        if char == 'R':
            add_str += 'r'
        elif char == 'r':
            add_str += 'R'
        elif char == 'U':
            add_str += 'u'
        elif char == 'u':
            add_str += 'U'
        elif char == 'B':
            add_str += 'b'
        elif char == 'b':
            add_str += 'B'
        else:
            add_str += f' {char}'
    return add_str[::-1]

def moves_to_string(move):
    if move == 'r_normal':
        add_str = 'R '
    elif move == 'r_prime':
        add_str = 'r '
    elif move == 'r_twice':
        add_str = '2r '
    elif move == 'u_normal':
        add_str = 'U '
    elif move == 'u_prime':
        add_str = 'u '
    elif move == 'u_twice':
        add_str = '2u '
    elif move == 'b_normal':
        add_str = 'B '
    elif move == 'b_prime':
        add_str = 'b '
    else:
        add_str = '2b '
    return add_str


all_moves = {0: 'r_normal', 1: 'r_prime', 2: 'r_twice',
             3: 'u_normal', 4: 'u_prime', 5: 'u_twice',
             6: 'b_normal', 7: 'b_prime', 8: 'b_twice'}

r_moved = {0: 'u_normal', 1: 'u_prime', 2: 'u_twice',
           3: 'b_normal', 4: 'b_prime', 5: 'b_twice'}

u_moved = {0: 'r_normal', 1: 'r_prime', 2: 'r_twice',
           3: 'b_normal', 4: 'b_prime', 5: 'b_twice'}

b_moved = {0: 'r_normal', 1: 'r_prime', 2: 'r_twice',
           3: 'u_normal', 4: 'u_prime', 5: 'u_twice'}

def move_dic(last_move):
    if last_move == 'R' or last_move == 'r' or last_move == 'r_twice':
        return r_moved
    elif last_move == 'U' or last_move == 'u' or last_move == 'u_twice':
        return u_moved
    elif last_move == 'B' or last_move == 'b' or last_move == 'b_twice':
        return b_moved
    else:
        return all_moves


solved_cube = Cube()
# mixed_cube = Cube(scramble=[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [6, 0], [5, 0], [7, 0]])
# mixed_cube = Cube()
# mixed_cube.move('b_prime')

# This is an 11-move solve! [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [6, 1], [5, 2], [7, 0]] 196 solutions
# Perm-t is a 10-move solve! [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [6, 0], [5, 0], [7, 0]] 20 solutions
# 3 rotated corners and perm-t is a 9 move solve! [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [6, 1], [5, 1], [7, 1]] 2
# 3 rotated corners is a 8-move solve! [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 1], [6, 1], [7, 1]] 8 solutions
# beginners placing corners is an 8-move! [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [7, 1], [5, 1], [6, 1]] 6 sols.

def solve_cube(mixed_cube):
    for depth in range(6):
        copy_dict = solved_cube.states.copy()
        for key in copy_dict:
            try:
                last_move = key[-1]
            except:
                last_move = 'l'
            dic_moves = move_dic(last_move)
            for move in dic_moves:
                move_str = dic_moves[move]
                solved_cube.cube = solved_cube.states[key].copy()
                solved_cube.move(move_str)
                # print(solved_cube.cube)
                solved_cube.states[key+moves_to_string(move_str)] = solved_cube.cube.copy()
                # print(solved_cube.states)
                # solved_cube.cube = solved_cube.states[key]
            del solved_cube.states[key]

        inter = intersection(solved_cube.states, mixed_cube.states)
        if inter is None:
            print(f'No solution yet in depth {depth}')
        else:
            return 2*(depth+1)-1, inter
            # break

        copy_dict = mixed_cube.states.copy()
        for key in copy_dict:
            try:
                last_move = key[-1]
            except:
                last_move = 'l'
            dic_moves = move_dic(last_move)
            for move in dic_moves:
                move_str = dic_moves[move]
                mixed_cube.cube = mixed_cube.states[key].copy()
                mixed_cube.move(move_str)
                mixed_cube.states[key+moves_to_string(move_str)] = mixed_cube.cube.copy()
                # mixed_cube.cube = mixed_cube.states[key]
            del mixed_cube.states[key]

        inter = intersection(solved_cube.states, mixed_cube.states)
        if inter is None:
            print(f'No solution yet in depth {depth}')
        else:
            return 2*(depth+1), inter
            # break
