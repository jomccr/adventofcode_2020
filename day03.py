#!/usr/bin/env python3

''' 
Part 1
------

You start on the open square (.) in the top-left corner and need to reach 
the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper 
model that prefers rational numbers); start by counting all the trees you 
would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is 
right 3 and down 1. Then, check the position that is right 3 and down 1 
from there, and so on until you go past the bottom of the map.

Starting at the top-left corner of your map and following a slope of right 
3 and down 1, how many trees would you encounter?
'''

from operator import mul 
from functools import reduce

class Coordinate:
    def __init__(self, x = 0, y = 0):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    def __getitem__(self, index):
        return self.position[index]

    def __add__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            return Coordinate(self.position[0] + other[0], self.position[1] + other[1])
        else: 
            return NotImplemented

def load_map(filename='./inputs/day03.input.txt'):
    with open(filename) as fh:
         return fh.read().splitlines()

def peek(m = ['.'], position = (0,0), slope=(0,0), x_boundary = 32):
    x, y = position
    dx, dy = slope
    line = ''
    try: 
        line = m[y + dy]
        try:
            return line[(x + dx) % x_boundary] 
        except IndexError as e:
            print(f'{e}, x={x}, dx={dx}') # shouldn't happen, so print debug info
    except IndexError: 
        return None # we've reached the bottom of the map

def count_trees(map = ['.'], slope = (3,1)):
    def is_tree(char):
        return char == '#' 
    
    count = 0
    ptr = Coordinate(0,0)

    height = len(map)
    width = len(map[0])

    while height > ptr[1]: 
        if is_tree(peek(m=map, position=tuple(ptr), slope=slope, x_boundary=width)):
            count += 1

        ptr += slope

    return count

grid = load_map()

part1_count = count_trees(grid, (3,1)) 
part2_count = [count_trees(grid, pos) for pos in [(1,1),(3,1),(5,1),(7,1),(1,2)]]

print('day 3 part 1', part1_count)
print('day 3 part 2', reduce(mul, part2_count, 1))

