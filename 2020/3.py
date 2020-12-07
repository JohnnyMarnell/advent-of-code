import gzip

def count_trees(dx, dy):
    trees = x = y = 0
    for row in rows:
        x = (x + dx) % len(row)
        y += dy
        if y < len(rows) and rows[y][x] == '#':
            trees += 1
    return trees

rows = gzip.open('inputs/3.gz').read().split('\n')
print(count_trees(3, 1))
print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))