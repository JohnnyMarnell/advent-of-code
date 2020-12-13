import gzip, re, json, collections, sys

wsize = 25
nums = [int(s) for s in gzip.open('inputs/9.gz').read().split('\n')]
sums = collections.defaultdict(lambda: 0)

for i in range(0, wsize):
    for j in range(i + 1, wsize):
        nsum = nums[i] + nums[j]
        sums[nsum] = sums[nsum] + 1

for i in range(wsize, len(nums)):
    global target_sum
    if nums[i] not in sums:
        target_sum = nums[i]
    
    for j in range(i - wsize + 1, i):
        osum = nums[i - wsize] + nums[j]
        sums[osum] = sums[osum] - 1
        if sums[osum] == 0:
            del(sums[osum])
        nsum = nums[j] + nums[i]
        sums[nsum] = sums[nsum] + 1

print(target_sum)

start = 0
size = 1
nsum = nums[0]
while start < len(nums) and start + size <= len(nums):
    if nsum < target_sum:
        size += 1
        if start + size <= len(nums):
            nsum += nums[start + size - 1]
    elif nsum > target_sum:
        nsum -= nums[start]
        start += 1
        size -= 1

    if nsum == target_sum:
        print(min(nums[start:start + size]) + max(nums[start:start + size]))
        break

    # print(nsum, start, start + size, size)