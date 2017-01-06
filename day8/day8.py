# coding: utf-8

import numpy

def read_input(filename):
    input = []
    for line in open(filename, 'r'):
        line = line.strip('\n')
        instruction = line.split(' ')
        input.append(instruction)
    return input

def parser_input(input):
    list_pixels = []
    nb_pixels = 0
    nb_column = 6
    nb_row = 50
    
    for i in range(0,nb_column):
        list_add = []
        for j in range(0,nb_row):
            list_add.append('0')
        list_pixels.append(list_add)
        
    for instruction in input:
        if instruction[0] == 'rect':
            rect(list_pixels, instruction[1])
            # print instruction
            # print numpy.array(list_pixels).reshape(nb_column, nb_row) # 这样就能以数组的形式打印出来了
            # print '\n'
            continue
        elif instruction[0] == 'rotate':
            rotate(list_pixels, instruction[-3], instruction[-1])
            # print numpy.array(list_pixels).reshape(nb_column, nb_row) 
            # print '\n'
            pass
        else:
            print 'wrong with ' + instruction[0] + instruction[-1]
            
    for i in range(0,nb_column):
        for j in range(0,nb_row):
            if list_pixels[i][j] == '1':
                nb_pixels += 1
    # return nb_pixels # part1
    return list_pixels

def rect(list, instruction):
    # row = int(instruction[0])
    # column = int(instruction[2])
    RandC = instruction.split('x')
    row = int(RandC[0])
    column = int(RandC[1]) 
    # global count 
    
    for i in range(0, column):
        for j in range(0, row):
            # if list[i][j] == '1':
                # print instruction
                # raw_input()
            list[i][j] = '1'
    return

def rotate(list, object, step):
    move = int(step)
    order = object.split('=')
    index = int(order[-1]) 
    # 妈的又是相似的问题，数字要有可能是两位数或一位数那就不能用下标操作了！！老老实实的split！！
    nb_row = 50
    nb_column = 6
    
    if object[0] == 'x':
        list_new = []
        for i in range(0, nb_column):
            list_new.append('0')
        for i in range(0, nb_column):
                pos = i + move
                if pos >= nb_column:
                    pos = pos - nb_column
                list_new[pos] = list[i][index]
        for i in range(0, nb_column):
            list[i][index] = list_new[i]
        
    elif object[0] == 'y':
        list_new = []
        for i in range(0, nb_row):
            list_new.append('0')
        for i in range(0, nb_row):
                pos = i + move
                if pos >= nb_row:
                    pos = pos - nb_row
                list_new[pos] = list[index][i]
        list[index] = list_new
  
    return

def print_code(list):
    new_list = []
    for i in range(0,10):
        list2 = []
        for j in range(0,6):
            list2.append(list[j][i*5: i*5 + 5])
        new_list.append(list2)
    return new_list
            
if __name__ == '__main__':
    #*************part1*************************    
    # global count
    # count = 0
    input = read_input('input.txt')
    # nb = 0
    # for one in input:
        # if one[0] == 'rect':
            # RandC = one[1].split('x')
            # r = int(RandC[0])
            # c = int(RandC[1]) 
            # nb += (r*c)
    # print nb
    # print parser_input(input)
    # print count
    #*************part2*************************      
    print numpy.array(print_code(parser_input(input)))
    
    print '\n'
    print 'All done baby!!'