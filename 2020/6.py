import gzip, re, json

def count_set_bits(num):
    bits = 0
    while (num > 0):
        bits += num & 1
        num >>= 1
    return bits

def letters_to_bits(s):
    s = s.lower()
    bits = 0
    for c in s:
        bits = bits | (1 << (ord(c) - ord('a')))
    return bits

with gzip.open('inputs/6.gz') as f:
    any_yes = 0
    all_yes = 0
    groups = re.split('\r?\n\r?\n', f.read())
    for group in groups:
        group_any_yes = 0
        group_all_yes = 0x3FFFFFFFF # all twenty six letters "on" to 1s, only 2 of last 25-28 bits, 0b0011 == 0x3
        for ans in re.split('\r?\n', group):
            ans = letters_to_bits(ans)
            group_any_yes = group_any_yes | ans
            group_all_yes = group_all_yes & ans
        any_yes += count_set_bits(group_any_yes)
        all_yes += count_set_bits(group_all_yes)
    print(any_yes)
    print(all_yes)
