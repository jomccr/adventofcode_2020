#!/usr/bin/env python3

def count_valid_pw_1(filename):
    num_valid_passwords = 0

    with open(filename) as fh:
        for line in fh: 
            n = 0
            rules, rule_char, password = line.split()
            rule_char = rule_char.split(':')[0]
            min_occur = int(rules.split('-')[0])
            max_occur = int(rules.split('-')[1])

            for char in password:
                if char == rule_char: 
                    n += 1

            if min_occur <= n <= max_occur: 
                num_valid_passwords += 1

    return num_valid_passwords

def count_valid_pw_2(filename):
    num_valid_passwords = 0

    with open(filename) as fh:
        for line in fh: 
            n = 0
            rules, rule_char, password = line.split()
            rule_char = rule_char.split(':')[0]
            idx1 = int(rules.split('-')[0])
            idx2 = int(rules.split('-')[1])

            validate_chars  = []

            try: 
                validate_chars += [password[idx1-1]]
            except IndexError:
                validate_chars.append(None)

            try: 
                validate_chars += [password[idx2-1]]
            except IndexError:
                validate_chars.append(None)

            if rule_char in validate_chars and validate_chars[0] != validate_chars[1]: 
                num_valid_passwords += 1

    return num_valid_passwords

print('day 2 part 1', count_valid_pw_1('./inputs/day02.input.txt'))
print('day 2 part 2', count_valid_pw_2('./inputs/day02.input.txt'))

