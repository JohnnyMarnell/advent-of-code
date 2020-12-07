import gzip, re, json

# translate to binary! plus ID formula is just decimal representation
# store in set, and look for missing ID
passes = [re.sub('B|R', '1', p) for p in gzip.open('inputs/5.gz').read().split('\n')]
passes = set([int(re.sub('F|L', '0', p), 2) for p in passes])
max = max(passes)
print(max)
for i in range(min(passes) + 1, max):
    if i not in passes:
        print i
        break