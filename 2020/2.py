import re
import gzip

def is_valid_part1(pw, letter, lower, upper):
    return lower <= pw.count(letter) <= upper

def is_valid_part2(pw, letter, lower, upper):
    return (pw[lower - 1] == letter) ^ (pw[upper - 1] == letter)

def count_valid(validator):
    valid = 0
    pattern = re.compile(r'^(\d+)-(\d+)\s+(.):\s+(.+)$')
    with gzip.open('inputs/2.gz') as f:
        for line in f:
            lower, upper, letter, pw = re.search(pattern, line).groups()
            if validator(pw, letter, int(lower), int(upper)):
                valid += 1
    return valid

print(count_valid(is_valid_part1))
print(count_valid(is_valid_part2))