#coding: utf

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
    value_a = 4
    while(1):
        print value_a
        value_b = []
        register_dic = {'a': value_a}
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
            elif direction[index][0] == 'jnz':
                index = fun_jnz(direction[index], register_dic, index)
            else:
                value_b.append(register_dic['b'])
                if register_dic['a'] == 0:
                    if verify_clock(value_b):
                        print value_b
                        return value_a
                    else:
                        break
        value_a += 1

def verify_clock(list):
    for i in range(0, len(list) - 1):
        if list[i] == list[i + 1]:
            return False
        else:
            pass
    return True
            
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
    return myindex
    

if __name__ == '__main__':
    #***********part1*************
    direction = read_file('input.txt')
    print det_register(direction)
    #***********part2*************
    
    print '\n'
    print 'All done baby !!'