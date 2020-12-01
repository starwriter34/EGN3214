# Advent Day of Code Day 1
#
# https://adventofcode.com/2020/day/1
#
# For Part 1 find the two sums that equal 2020 and then multiply them
# For Part 2 find the three sums that equal 2020 and then multiply them
def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(line[:-1]) for line in f.readlines()]

def part1(mylist):
    for a in mylist:
        if (2020 - a) in mylist:
            return (2020 - a) * a

def part2(mylist):
    for a in range(len(mylist)):
        for b in range(a, len(mylist)):
            if (2020 - mylist[a] - mylist[b]) in mylist:
                return mylist[a]*mylist[b]*(2020-mylist[a]-mylist[b])

mylist = readFile()
print(f'Part 1: {part1(mylist)}')
print(f'Part 2: {part2(mylist)}')
            