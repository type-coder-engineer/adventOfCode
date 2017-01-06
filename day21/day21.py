# coding: utf
import math, copy

def read_file(filename):
    list_directions = []
    for line in open(filename, 'r'):
        line = line.strip('\n')
        words = line.split(' ')
        list_directions.append(words)
    return list_directions
    
def treat_string(mystring, list):
    # mystring = 'abcdefgh'
    # mystring = 'abcde'
    for direction in list:
        mystring = follow(direction, mystring)
        # print direction
        # print mystring
        # raw_input()
    return mystring
        
def follow(direction, string):
    string_list = []
    for letter in string:
        string_list.append(letter)
        
    if direction[0] == 'swap':
        if direction[1] == 'position':
            pos1 = int(direction[2])
            pos2 = int(direction[5])
        else:
            pos1 = int(string_list.index(direction[2]))
            pos2 = int(string_list.index(direction[5]))
        string_list[pos1], string_list[pos2] = string_list[pos2], string_list[pos1]
    
    elif direction[0] == 'move':
        pos_del = int(direction[2])
        pos_insert = int(direction[5])
        move = string_list[pos_del]
        del string_list[pos_del]
        string_list.insert(pos_insert, move)
    
    elif direction[0] == 'reverse':
        pos1 = float(direction[2])
        pos2 = float(direction[4])
        # print pos1, pos2
        # print math.ceil(float((pos2 - pos1)/2))
        for i in range(0, int(math.ceil((pos2 - pos1)/2))):
            # print string_list[pos1 + i], string_list[pos2 - i]
            string_list[int(pos1) + i], string_list[int(pos2) - i] = string_list[int(pos2) - i], string_list[int(pos1) + i]
            
    else:
        if direction[1] == 'based':
            nb_rotate = int(string_list.index(direction[-1]))
            if nb_rotate >= 4:
                nb_rotate += 1
            nb_rotate += 1
            string_list = rotate_list('right', nb_rotate, string_list)
        else:
            if direction[1] == 'left':
                nb_rotate = int(direction[2])
                string_list = rotate_list('left', nb_rotate, string_list)
            else:
                nb_rotate = int(direction[2])
                string_list = rotate_list('right', nb_rotate, string_list)
                          
    return ''.join(string_list[0:])
    
def rotate_list(direction, steps, list):
    list_new = []
    if direction == 'left':
        for i in range(0, len(list)):
            replace_index = i + steps
            if replace_index >= len(list):
                replace_index -= len(list)
            list_new.append(list[replace_index])
    else:
        for i in range(0, len(list)):
            replace_index = i - steps
            if replace_index < 0:
                replace_index += len(list)
            list_new.append(list[replace_index])
    # print list_new
    return list_new
 
 # 这里如果在形参中设置一个solution并不能正确的返回，所以可以设一个全局变量，然后就能到在最后返回string到main了
def decoding(mystring, list, list_input):
    global solution
    if len(solution) != 0:
        return solution
    if len(list) == 0:
        # print mystring
        if decode(mystring, list_input):
            # print mystring
            solution = mystring
            # print solution
        return  
    else:
        # print list
        initial_list = copy.copy(list)
        initial_string = mystring
        for i in range(0, len(list)):
            mystring = initial_string
            mystring += list[i]
            del list[i]
            decoding(mystring, list, list_input)
            list = copy.copy(initial_list)
        # raw_input()
    return solution
    
def decode(password, list_input):
    code = 'fbgdceah'
    out = treat_string(password, list_input)
    if out == code:
        return True 
    else:
        return False
    
if __name__ == '__main__':
#**************part1*****************
    # list = ['a','b','c']
    # list = rotate_list('left', 1, list)
    list_input = read_file('input.txt')
    # list_input = read_file('test.txt')
    # print treat_string(list_input)
#**************part1*****************
    mystring = 'abcdefgh'
    mylist = []
    for letter in mystring:
        mylist.append(letter)
    # global count
    # count = 0
    global solution
    solution = ''
    print decoding('', mylist, list_input)
    
    print '\n'
    print 'All done baby!!'