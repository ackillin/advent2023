import re

# Hashing Algorithm
def get_hash(line):
    total = 0
    for let in line:
        total = (total+ord(let)) * 17 % 256
    return int(total)


print('part 1:',sum([get_hash(x)
         for x in open('txt15.txt').readlines() for x in x.strip().split(',')]))


# Part 2
box = [{} for i in range(256)]  # 256 Dictionaries
f = lambda a: int(get_hash(a))

for x in open('txt15.txt'):
    for line in x.strip().split(','):
        if '=' in line:
            line = re.split(r'[=-]', line, 1)
            box[f(line[0])][line[0]] = int(line[1])
        else:
            line = re.split(r'[=-]', line, 1)
            if box[f(line[0])].get(line[0]):
                box[f(line[0])].pop(line[0])

total = 0
for counter, x  in enumerate(box):
    counter +=1
    for val_count, val in enumerate(x.values()):
        val_count +=1
        total += (counter * val_count * val)

print('part 2:',total)

print('Part 1 :', sum([(val:=0) or [val:=(val+ord(c))*17%256 for c in s] and val
                       for s in open('txt15.txt').read().strip().split(',') ]) )
