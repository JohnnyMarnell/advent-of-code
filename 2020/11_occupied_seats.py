import gzip, re, json, collections, sys, copy

seat_map = [list(s) for s in gzip.open('inputs/11.gz').read().split('\n')]
next_map = None
rows = len(seat_map)
cols = len(seat_map[0])

def move():
    unmoved = True
    for r in range(0, rows):
        for c in range(0, cols):
            if seat_map[r][c] == '.':
                continue
            elif seat_map[r][c] == 'L' and count_occ(r, c) == 0:
                next_map[r][c] = '#'
                unmoved = False
            elif seat_map[r][c] == '#' and count_occ(r, c) >= 4:
                next_map[r][c] = 'L'
                unmoved = False
    return unmoved

def count_occ(r, c):
    return count(r - 1, c - 1) + count(r - 1, c) + count(r - 1, c + 1) \
         + count(r,     c - 1) +                   count(r,     c + 1) \
         + count(r + 1, c - 1) + count(r + 1, c) + count(r + 1, c + 1)

def count(r, c):
    return 1 if r >= 0 and r < rows and c >= 0 and c < cols and seat_map[r][c] == '#' else 0

while True:
    next_map = copy.deepcopy(seat_map)
    if move():
        break
    seat_map = next_map

print(sum([sum([1 if seat == '#' else 0 for seat in row]) for row in seat_map]))