import re
from pprint import pprint
import numpy as np
import threading

res = []

# After seeds:
# end start range
def get_input(file_name):
    seeds = 0
    directions = {}
    curr_name = ''
    with open(file_name) as file:
        for line in file:
            if line[0:5] == 'seeds':
                seeds= re.findall(r'\d+', line)
            else:
                if re.search('-',line):
                    curr_name = line.strip()
                    directions[curr_name] = []
                elif re.search('\d+',line):
                    directions[curr_name].append(re.findall('\d+',line))
    return seeds, directions

def conv_seeds(seeds):
    for x in range(len(seeds)):
        seeds[x] = int(seeds[x])
    return seeds


def is_seed(direc, seeds):
    for x,y in enumerate(seeds):
        print(direc)
        if y in np.arange(direc[1], direc[1]+direc[2]):
            return x,y
    return (None, None)


def reset_seeds(seeds):
    for x,y in enumerate(seeds):
        seeds[x][1] = False
    return seeds

def get_seed_range(seeds):
    new_seed = list(range(seeds[0], seeds[0]+seeds[1]))
    new_seed += range(seeds[2], seeds[2] + seeds[3])
    return new_seed

# Direction: Destination, Source, Range
def part1(seeds, directions):
    for x in range(len(seeds)):
        seeds[x] = [seeds[x],False]
    for map, ranges in directions.items():
        #pprint(ranges)
        for direc in ranges:
            #If it is in inside the range
            for x, y in enumerate(seeds):
                value = seeds[x][0]
                if not seeds[x][1] and (value > direc[1] and value < direc[1] + direc[2]):
                    if seeds[x][1] == False:
                        seeds[x][0] = abs(direc[1]-value) + direc[0]
                        seeds[x][1] = True
        seeds = reset_seeds(seeds)
    seeds = [seeds[x][0] for x,y in enumerate(seeds)]
    res.append(min(seeds))
    return seeds


def part2(seeds, directions, step=1):
    for counter in range(0,len(seeds),2):
        print(f'part {counter} start')
        base = seeds[counter]
        div = seeds[counter+1]//12
        #print(base,div)
        result = []
        threads = []
        for x in range(1,13):
            t = threading.Thread(target=part1, args = (list(range(base + div*(x-1), base + div*x, step)) ,directions))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

def get_step(directions):
    smallest = list(directions.values())[0][0][2]
    for section in list(directions.values()):
        for command in section:
            if smallest > command[2]:
                smallest = command[2]
    return smallest


def incrementally_smallest(seeds,directions,step):
    while step > 10:
        step = step//10
        ind = res.index(min(res))
        seeds = seeds[:]
        part2()  # Main looping
        res = []


if __name__ == '__main__':
    seeds, directions = get_input('txt5.txt')
    seeds = conv_seeds(seeds)
    for x,v in directions.items():
        directions[x] = [conv_seeds(j) for j in v]
    #part1(seeds,directions)
    step = get_step(directions)
    part2(seeds,directions,step)
    print(res)
    print(min(res))
    ind = res.index(min(res))
    print(ind%len(seeds)//2)
    ind = ind%len(seeds)//2
    res = []
    print(seeds[ind-1:ind+1])
    part2(seeds[ind-1:ind+1], directions, step//10)
    print(res)
    print(min(res))
    print(seeds)
    #17738291 -- too high
    #17738291
    #17729182
