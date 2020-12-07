import gzip

# Use a hash set, for fast lookup if we have needed remainder
# We can add as we iterate (at loop end to avoid double counting 1010)
# O(n) time
expenses = set()
with gzip.open('inputs/1.gz') as f:
    for line in f:
        expense = int(line)
        remainder = 2020 - expense
        if remainder in expenses:
            print(expense * remainder)
        expenses.add(expense)

# for part 2, we need to enumerate all pairs, can do this by starting at left end
# and iterating all to the right pairs, inc left and repeat (all unique 2 combinations, not permutations)
# reuse hash for fast lookup of needed sum tuple's third
arr = list(expenses)
for i in range(1, len(arr)):
    for j in range(i + 1, len(arr)):
        remainder = 2020 - arr[i] - arr[j]
        if remainder in expenses:
            print(arr[i] * arr[j] * remainder)