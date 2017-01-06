# coding:utf 
import time

def read_file(filename):
    list_directions = []
    for line in open(filename, 'r'):
        line = line.strip('\n')
        words = line.split(' ')
        while('' in words):
            words.remove('')
        list_directions.append(words)
    return list_directions
    
def det_register(direction):
    register_dic = {'a': 12}
    index = -1
    while(1):
        index += 1
        if index >= len(direction):
            break
        if direction[index][0] == 'cpy':
            fun_cpy(direction[index], register_dic)
        elif direction[index][0] == 'inc':
            fun_inc(direction[index], register_dic)
        elif direction[index][0] == 'dec':
            fun_dec(direction[index], register_dic)
        elif direction[index][0] == 'tgl':
            fun_tgl(direction, register_dic, index)
        else:
            index = fun_jnz(direction[index], register_dic, index)
            
        if index == 16:
            print register_dic['c']
            print register_dic
            # raw_input()
    return register_dic['a']
    
def fun_cpy(direction, dic):
    if direction[1] in dic:
        dic[direction[2]] = dic[direction[1]]
    else:
        try:
            dic[direction[2]] = int(direction[1])
        except:
            pass
    return
    
def fun_inc(direction, dic):
    if direction[1] in dic.keys():
        dic[direction[1]] += 1 
    else:
        pass
    return

def fun_dec(direction, dic):
    if direction[1] in dic.keys():
        dic[direction[1]] -= 1
    else:
        pass
    return

def is_nb(string):
    try:
        int(string)
        return True
    except:
        return False
            
def fun_jnz(direction, dic, index): 
    myindex = index
    if is_nb(direction[1]):
        if int(direction[1]) != 0:
            if is_nb(direction[2]):
                myindex += (int(direction[2]) - 1)
            else:
                myindex += (dic[direction[2]] - 1)
        else:
            pass
    else:
        if direction[1] in dic.keys():
            if dic[direction[1]] != 0:
                myindex += (int(direction[2]) - 1)
            else:
                pass
        else:
            pass
    # print myindex
    # raw_input()
    return myindex
    
def fun_tgl(direction, dic, index):
    # print index
    # print direction[index][1]
    # print direction
    if direction[index][1] in dic.keys():
        index_change = index + dic[direction[index][1]]
        # print dic[direction[index][1]]
    else:
        index_change = index + int(direction[index][1])
        # print int(direction[index][1])
    # print direction[1]
    # print index
    # print len(direction)
    # print direction[index_change][0]
    if index_change >= len(direction):
        return
    if len(direction[index_change]) == 2:
        if direction[index_change][0] == 'inc':
            direction[index_change][0] = 'dec'
        else:
            direction[index_change][0] = 'inc'
    else:
        if direction[index_change][0] == 'jnz':
            direction[index_change][0] = 'cpy'
        else:
            direction[index_change][0] = 'jnz'
    # print direction
    # print dic
    return 
    
if __name__ == '__main__':
    #***********part1*************
    list = read_file('input.txt')
    print det_register(list)
    # end = int(round(time.time()*1000))    
    # print end - start
    #***********part2*************  
    print '\n'
    print 'All done baby !!'