from aocd import get_data
import re
num_conv = {'one': 'one1one', 'two':'two2two','three':'three3three','four':'four4four','five':'five5five','six':'six6six','seven':'seven7seven','eight':'eight8eight','nine':'nine9nine'}

def ret_num():
    return num_conv

def replace(data):
    for line in data:
        for name,num in num_conv.items():
            line = line.replace(name,num)
        yield line

def summary(data):
    for line in data:
        mat1 = re.search(r'\d',line)
        if mat1:
            mat2 = re.search(r'\d',line[::-1])
            mat1 = mat1.group(0) + mat2.group(0)
        else:
            mat1 = '0'
        yield int(mat1) * 11 if len(mat1) == 1 else int(mat1)

def summary2(data):
    for line in data:
        pass

def get_inputs(file_name):
    listy = []
    with open(file_name) as file:
        for line in file:
            listy.append(line.strip())
    return listy

if __name__ == '__main__':
    #input = get_data(day=1,year=2023)
    input = get_inputs('txt1.txt')
    inputs = replace(input)
    h  = list(summary(inputs))
    print(sum(h))
