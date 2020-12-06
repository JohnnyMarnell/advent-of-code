import gzip
expenses = set()
with gzip.open('inputs/1.gz') as f:
    for line in f:
        expense = int(line)
        remainder = 2020 - expense
        if remainder in expenses:
            print(expense * remainder)
            break
        expenses.add(expense)