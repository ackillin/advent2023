import re
import numpy as np


# Hashing Algorithm
def get_hasd(line):
    total = 0
    for let in line:
        total = (total+ord(let)) * 17 % 256
    return int(total)


print('part 1:',sum([get_hasd(x)
         for x in open('txt15.txt').readlines() for x in x.strip().split(',')]))


# Part 2
box = [{} for i in range(256)]
u = lambda a: int(get_hasd(a))
#print( [ box[u(line)].append((line[:2],int(line[3]))) if line[2] == '=' else box[u(line))].remove(line[:2])  for x in open('test.txt').readlines() for line in x.strip().split(',')] )

for x in open('txt15.txt'):
    for line in x.strip().split(','):
        if '=' in line:
            line = re.split(r'[=-]', line,1)
            #print(box[u(line)])
            box[u(line[0])][line[0]] = int(line[1])
        else:
            line = re.split(r'[=-]', line,1)
            if box[u(line[0])].get(line[0]):
                box[u(line[0])].pop(line[0])
#print(box)

total = 0
for counter,x  in enumerate(box):
    counter +=1
    for keys, val in enumerate(x.values()):
        keys +=1
        #print(counter * keys * val)
        total += (counter * keys * val)

print('part 2:',total)
