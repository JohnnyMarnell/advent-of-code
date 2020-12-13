import gzip, re, json

required = 'byr iyr eyr hgt hcl ecl pid'.split(' ')

def parse_passport(lines):
    passport = {}
    for field in re.split('\s+', lines):
        pair = field.split(':')
        if passport.get(pair[0]) is not None:
            print "******** dupe \n\n\n\n\n\n"
        passport[pair[0]] = pair[1]
    # passport['original'] = lines
    return passport

def is_valid_part1(passport):
    return all(key in passport for key in required)

def is_valid_part2(passport):
    valid = is_valid_part1(passport) \
        and in_range(passport['byr'], 1920, 2002) \
        and in_range(passport['iyr'], 2010, 2020) \
        and in_range(passport['eyr'], 2020, 2030) \
        and (  re.match('\d+\s*cm', passport['hgt']) and in_range(passport['hgt'], 150, 193) \
            or re.match('\d+\s*in', passport['hgt']) and in_range(passport['hgt'], 59, 76)) \
        and re.match('#[a-f0-9]{6}', passport['hcl']) \
        and re.match('amb|blu|brn|gry|grn|hzl|oth', passport['ecl']) \
        and re.match('\d{9}', passport['pid'])
    # print(bool(valid), json.dumps(passport))
    if valid:
        # print(json.dumps(passport))
        keys = list(passport.keys())
        keys.sort()
        print([key + ':' + passport[key] for key in passport])
    return valid


def in_range(string, min, max):
    return min <= int(''.join(filter(str.isdigit, string))) <= max

def count_valid(validator):
    valid = 0
    passports = gzip.open('inputs/4.gz').read().split('\n\n')
    for passport in passports:
        passport = parse_passport(passport)
        if validator(passport):
            valid += 1
    return valid

# print(count_valid(is_valid_part1))
# print(count_valid(is_valid_part2))

count_valid(is_valid_part2)