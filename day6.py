import re



def get_inputs(file_name):
    listy = []
    with open(file_name) as file:
        for line in file:
            line = re.findall(r'\d+',line)
            line = [int(x) for x in line]
            listy.append(line)
    return listy

def part1(listy):
    num_ways = []
    for counter, time in enumerate(listy[0]):
        distance = listy[1][counter]
        # For each time inside the list
        num_ways.append(0)
        for cur_time in range(time):
            remaining_time = time-cur_time
            if (cur_time * remaining_time) > distance:
                num_ways[-1] +=1
    return num_ways

def get_multi(things):
    total = 1
    for x in things:
        total *= x
    return total

def part2(listy):
    new_line = []

    for x in listy:
        line = ''
        for i in x:
            line += str(i)
        new_line.append([int(line)])
    return new_line

inputs = get_inputs('txt6.txt')
#print(part1(inputs))
#print(get_multi(part1(inputs)))
new_input = part2(inputs)
print(new_input)
print(part1(new_input))
