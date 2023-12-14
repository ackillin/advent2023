import re

def get_inputs(file_name):
    with open(file_name,'r') as file:
        for line in file:
            yield line.strip().replace('.',' ')


def get_sym_nums(data):
    # First get the x, y of the number as well as how long it is
    # Idea: Look to the right and left first
    sym_list = []
    num_list = []
    for line_num in range(len(data)):
        #print(data[line_num])
        for x in re.finditer('\d+',data[line_num]):
            if len(x.group(0)) == 1:
                num_list.append([line_num,(x.span()[0],x.span()[0]),int(x.group(0)),False] )
            else:
                num_list.append([line_num,(x.span()[0], x.span()[1]-1),int(x.group(0)),False])
        for x in re.finditer('[^\s\d]',data[line_num]):
            sym_list.append((line_num,x.span()[0], x.group(0)))

    return sym_list, num_list



#Num format: row, (col start, col end), value, checked
def get_around(point, num_list):
    x = point[0]
    y = point[1]
    #print(x,y)
    around = [(x-1,y-1),(x,y-1),(x+1,y-1),
              (x-1,y),(x,y),(x+1,y),
              (x-1,y+1),(x,y+1),(x+1,y+1)]
    for num in range(len(num_list)):
        number = num_list[num]
        # Check if either the beginning number or end number is around
        if (number[0], number[1][0]) in around or (number[0], number[1][1]) in around:
            num_list[num][3] = True
    return num_list  # Updated num_list to now have trues, if true


def all_false(num_list):
    for x in range(len(num_list)):
        num_list[x][3] = False
    return num_list

def remove_nums(sym_list,num_list, part = 1):
    if part == 2:
        total = 0
        for point in sym_list:
            count = []
            #Part 2, change the wrapper to 1
            if point[2] == '*':
                num_list = get_around(point, num_list)

                for x in num_list:
                    if x[3] == True:
                        count.append(x)
                if len(count) == 2:
                    total += (count[0][2] * count[1][2])
                num_list = [ [num_list[x][0], num_list[x][1], num_list[x][2], False]  for x in range(len(num_list))]
        return total
    else:
        for point in sym_list:
            num_list = get_around(point, num_list)
        # Sum
        total = 0
        for num in num_list:
            if num[3] == True:
                total+=num[2]
        return total


def wrapper(data):
    sym, num = get_sym_nums(data[:])
    print(remove_nums(sym,num,2))


if __name__ == "__main__":
    inputs = list(get_inputs('txt3.txt'))
    #inputs = list(replace_all(inputs))
    #print(inputs)
    wrapper(inputs)
