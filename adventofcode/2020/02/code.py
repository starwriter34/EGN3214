'''
https://adventofcode.com/2020/day/2
####################
       Part 1
####################

--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

####################
       Part 2
####################

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
'''

def readFile() -> list:
    input_list = list()
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        for line in f.readlines():
            txt = line.split()
            nums = txt[0].split("-")
            # Sample Line before: 13-16 k: kkkkkgmkbvkkrskhd
            input_list.append((int(nums[0]), int(nums[1]), txt[1][:1], txt[2]))
    return input_list

def part1(mylist):
    password_valid = 0
    for line in mylist:
        num_min, num_max, check, password = line
        count = password.count(check)
        if count >= num_min and count <= num_max:
            password_valid += 1

    return password_valid

def part2(mylist):
    password_valid = 0
    for line in mylist:
        num_min, num_max, check, password = line
        if (password[num_min-1] == check) ^ (password[num_max-1] == check):
            password_valid += 1

    return password_valid
    
def test():
    test_input = [
        (1,3,'a','abcde'),
        (1,3,'b','cdefg'),
        (2,9,'c','ccccccccc'),
    ]
    assert part1(test_input) == 2
    assert part2(test_input) == 1

test()
mylist = readFile()
print(f'Part 1: {part1(mylist)}')
print(f'Part 2: {part2(mylist)}')
