import gzip, re, json

# translate to binary! plus ID formula is just decimal representation
# store in set, and look for missing ID
with gzip.open('inputs/5.gz') as f:
    passes = [re.sub('B|R', '1', bpass) for bpass in f.read().split('\n')]
    passes = set([int(re.sub('F|L', '0', bpass), 2) for bpass in passes])
    max = max(passes)
    print(max)
    for i in range(min(passes) + 1, max):
        if i not in passes:
            print i
            break