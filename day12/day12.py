# coding: utf-8

def read_input(filename):
    list_input = []
    for line in open(filename, 'r'):
        line = line.strip('\n')
        words = line.split(' ')
        list_input.append(words)
    return list_input
    
def parser_input(input):
    dic_register = {'c':1} # part2 initialise 'c' as 1
    index = -1
    nb = 1
    while(1):
        index += 1
        # if index == 10 or index == 18:
            # nb += 1
        # print index
        if index >= len(input):   
            break  
        # if 'b' in dic_register.keys():
            # print dic_register['b']
            # raw_input()
        if input[index][0] == 'inc':
            inc(dic_register, input[index][1])
        elif input[index][0] == 'dec':
            dec(dic_register, input[index][1]) 
        elif input[index][0] == 'cpy':
            cpy(dic_register, input[index][1], input[index][2])
        elif input[index][0] == 'jnz':
            try:
                value = int(input[index][1])
                if value != 0:
                    index += (int(input[index][2]) - 1)
                continue
            except:
                if input[index][1] not in dic_register.keys():
                    continue
                if dic_register[input[index][1]] != 0:
                    index += (int(input[index][2]) - 1)
                else:
                    pass                
    # print dic_register['c']
    # print dic_register['d']   
    return dic_register['a']   
    
def inc(dic, register):
    dic[register] += 1
    return
    
def dec(dic, register):
    dic[register] -= 1
    return 

def cpy(dic, value, register):
    if value in dic.keys():
        value = dic[value]
    dic[register] = int(value)
    return
    
if __name__ == '__main__':
    #*************part1*************************    
    input = read_input('input.txt')
    # print input
    print parser_input(input)
    #*************part2*************************      
    
    print '\n'
    print 'All done baby!!'