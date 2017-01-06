# coding: utf-8

def read_input(filename):
    list_input = []
    target = open(filename, 'r')
    for line in target:
        line = line.strip('\n')
        words = line.split(' ')
        list_input.append(words)
    return list_input

def parser_input(list):
    bot_dic = {}
    index = -1
    order_done = []
    output_dic = {}        
    while(1):
        index += 1
        if index >= len(list):
            index = 0
        if list[index][0] == 'value' and index not in order_done:
            parser_value(bot_dic, list[index])
            order_done.append(index)
        elif list[index][0] == 'bot':
            if parser_give(bot_dic, list[index], output_dic):
                return output_dic['0']*output_dic['1']*output_dic['2']
            else:
                pass
            
def parser_value(dic, order):
    value_add = int(order[1])
    if order[-1] not in dic.keys():
        dic[order[-1]] = [value_add]
    else:
        dic[order[-1]].append(value_add)
    return 

def parser_give(dic, order, output):
    if order[1] not in dic:
        return False
    elif len(dic[order[1]]) < 2:
        return False
    else:
        # print dic[order[1]]
        flag_bot_low = True
        flag_bot_high = True
        if order[5] == 'bot':
            bot_low = order[6]
        else:
            flag_bot_low = False
        if order[-2] == 'bot':
            bot_high = order[-1]
        else:
            flag_bot_high = False
        list_values = dic[order[1]]
        list_values.sort() # 妈的这个不知道之前有没有遇到，list中是string不是int，所以sort的结果不一定是从小到大，比如'21'就在'3'前面。。
        # print list_values
        dic[order[1]] = []
        if flag_bot_low:
            if bot_low not in dic.keys():
                dic[bot_low] = [list_values[0]]
            else:
                dic[bot_low].append(list_values[0])
        else:
            output[order[6]] = list_values[0]
        if flag_bot_high:
            if bot_high not in dic.keys():
                dic[bot_high] = [list_values[1]]
            else:
                dic[bot_high].append(list_values[1])   
        else:
            output[order[-1]] = list_values[1]
        # if list_values[0] == 17 and list_values[1] == 61:
            # return True  # part1
        if '0' in output.keys() and '1' in output.keys() and '2' in output.keys():
            return True
        else:
            return False
            
if __name__ == '__main__':
#*************part1*************************  
    list_input = read_input('input.txt')
    # print list_input
    print parser_input(list_input)

 #*************part2************************* 

    print '\n'
    print 'All done baby!!'