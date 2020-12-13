import gzip, re, json, collections, sys, heapq

# adapters = [int(s) for s in gzip.open('inputs/10.gz').read().split('\n')]
adapters = [int(s) for s in gzip.open('/tmp/z').read().split('\n')]
adapters.append(3 + max(adapters))
heapq.heapify(adapters)
copy = list(adapters)

jolts = 0
diff_1 = 0
diff_3 = 0

while len(adapters):
    next_adapter = heapq.heappop(adapters)
    diff = next_adapter - jolts
    if diff == 1:
        diff_1 += 1
    elif diff == 3:
        diff_3 += 1
    elif diff > 3 or diff < 0:
        print('Not enough jiggawatts in the joltage')
    jolts = next_adapter

print(diff_1 * diff_3)

configs = 0
def enumerate_configs(adapters, index, jolts):
    global configs
    print(index, jolts)
    if index >= len(adapters) - 1:
        configs += 1
        return
    for i in range(index, min(index + 3, len(adapters))):
        if adapters[i] - jolts <= 3:
            enumerate_configs(adapters, i + 1, jolts + adapters[i])

enumerate_configs(copy, 0, 0)
print(configs)