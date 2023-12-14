import re
from pprint import pprint
import math


def get_inputs(filename):
    instruct = []
    maps = {}
    get_two = lambda line: re.sub(r'\s|\(|\)','',line[1]).split(',')
    with open(filename) as file:
        for line in file:
            line = line.strip().split('=')
            if len(line) == 1:
                instruct.append(line[0])
            else:
                two = get_two(line)
                maps[line[0].strip()] = (two[0],two[1])
    return instruct[0], maps


def part2_check(current):
    for i in current:
        if i in good_matches:
            return True
    return False

def part1(maps,instruct):
    found = False
    length_instruct = len(instruct)
    counter = 0
    matches = re.findall
    all = list(set(re.findall(r'[A-Z]+A', str(maps.keys()) )))
    all.sort()
    nums = []
    good_matches = ('ZZZ','TNZ','SJZ','GNZ','NMZ','BNZ')
    for current in all:
        found = False
        counter = 0
        curr = current
        while not found:
            if curr in good_matches:
                print(f'{current} to {curr} in {counter} steps')
                nums.append(counter)
                found = True
            if instruct[counter%len(instruct)] == 'L':
                curr = maps[curr][0]
            else:
                curr = maps[curr][1]
            counter +=1
    print(nums)
    return math.lcm(*nums)


if __name__ == "__main__":
    instruct, maps = get_inputs('txt8.txt')
    print(part1(maps, instruct))
