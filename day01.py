#!/usr/bin/env python3

import itertools
from functools import reduce 

aoc_input = [int(line) for line in open('./inputs/day01.input.txt')]

def find_twosum(input_values, target=2020):
    input_counts = {}

    for num in input_values:
        input_counts[num] = input_counts.get(num, 0) + 1 

    for num in input_counts:
        match = target - num
        answer = input_counts.get(match, None)

        if answer: 
            return num * match

# generic uses functional programming and itertools 
def find_ksum(input_values, count=2, target=2020):
    for combo in itertools.combinations(input_values, r=count):
        if sum(combo) == target: 
            return reduce(lambda x, y: x*y, combo)

print('day 1 part 1', find_twosum(aoc_input))
print('day 1 part 2', find_ksum(aoc_input, count=3))

