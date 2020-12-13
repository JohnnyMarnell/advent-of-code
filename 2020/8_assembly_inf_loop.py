import gzip, re, json, collections, sys

insts = gzip.open('inputs/8.gz').read().split('\n')
ran = collections.defaultdict(lambda: False)

def run(index, acc):
    if index >= len(insts):
        print('Finished.', acc)
        sys.exit(0)
    ran[index] = True
    cmd, amt = insts[index].split(' ')
    amt = int(amt)
    if cmd == 'jmp':
        if ran[index + amt]:
            print('Already run, treating as no-op, acc val:', acc)
            run(index + 1, acc)
        run(index + amt, acc)
    elif cmd == 'acc':
        run(index + 1, acc + amt)
    else:
        run(index + 1, acc)

run(0, 0)