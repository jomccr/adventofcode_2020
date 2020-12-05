#!/usr/bin/env python3
import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

def valid_hgt(height):
    if height[-2:] == 'cm': return 150 <= int(height[:-2]) <= 193
    if height[-2:] == 'in': return 59 <= int(height[:-2]) <= 76

# building a lookup table of callable validation rules - probably a dirty hack
valid = { }

valid['byr'] = lambda val: 1920 <= int(val) <= 2002
valid['iyr'] = lambda val: 2010 <= int(val) <= 2020
valid['eyr'] = lambda val: 2020 <= int(val) <= 2030
valid['hgt'] = valid_hgt
valid['hcl'] = lambda val: re.findall('^#(?:[0-9a-f]{3}){1,2}$', val) != []
valid['ecl'] = lambda val: val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valid['pid'] = lambda val: re.findall('^([0-9]){9}$', val) != []
valid['cid'] = lambda val: True

# This function is the worst. My disappointment is immeasurable, and my day has been ruined.
def parse(passport_file):
    db = []
    passport_data = [attributes.split(' ') for attributes in [line.replace('\n', ' ').strip() for line in passport_file.split('\n\n')]]
    for line in passport_data:
        db.append({ attr: val for (attr, val) in [data.split(':') for data in [entry for entry in line]] })
    return db

def validate_fields(data, fields):
    missing_keys = []
    for key in fields:
        if key not in data.keys():
            missing_keys.append(key)

    if len(missing_keys) == 0 or (missing_keys == ['cid']):
        return True

    return False

def validate_passport(data):
    return all([valid[key](val) for key, val in data.items()])

def part1(filename='./inputs/day04.input.txt'):
    ''' count number of passports with all required fields '''
    with open(filename) as fh:
        passport_data = parse(fh.read())
        return list(validate_fields(row, required_fields) for row in passport_data).count(True)

def part2(filename='./inputs/day04.input.txt'):
    '''Count number of passports in file that are VALID'''
    with open(filename) as fh:
        passport_data = parse(fh.read())
        return list(validate_passport(data) and validate_fields(data, required_fields) for data in passport_data).count(True)


print('day 4 part 1', part1())
print('day 4 part 2', part2())

