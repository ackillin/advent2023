import re

def get_inputs(file_name):
    winning, nums = [],[]
    count, matches = [], []
    with open(file_name) as file:
        for line in file:
            multi = 0
            line = line.strip().split('|')
            winning.append(re.findall(r'\d+',line[0])[1:])
            nums.append(re.findall(r'\d+',line[1].strip()))
            matches.append(0)
            for x in nums[-1]:
                if x in winning[-1]:
                    matches[-1]+=1
                    if multi == 0:
                        multi = 1
                    else:
                        multi *= 2
            count.append(multi)
    return winning, nums, count, matches


if __name__ == '__main__':
    winning, nums, count, matches = get_inputs('txt4.txt')
    print(sum(count))
    total = [1] * len(matches)
    for counter, num in enumerate(matches):
        for j in range(num):
            total[counter + j + 1] += total[counter]
    print(sum(total))
