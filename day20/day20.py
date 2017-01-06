# coding: utf-8

def read_input(filename):
    list_range = []
    for line in open(filename, 'r'):
        line = line.strip('\n')
        two_nbs = line.split('-')
        smaller = int(two_nbs[0])
        bigger = int(two_nbs[1])
        list_range.append([smaller, bigger])
    return list_range
    
def order_ips(list):
    value_dic = {}
    for one in list:
        value_dic[one[0]] = one[1]
    values_high = value_dic.values()
    values_high.sort()
    for value in values_high:
        flag_ok = True
        for value_low, value_high in value_dic.items():
            if value_low < value and value_high > value:
                flag_ok = False
                break
            else:
                pass
        if flag_ok:
            break
        else:
            pass
    return value + 1

def total_ips(list):
    total = 0
    value_dic = {}
    for one in list:
        value_dic[one[0]] = one[1]
    values_high = value_dic.values()
    values_low = value_dic.keys()
    values_high.sort()
    values_low.sort()
    for value in values_high:
        flag_ok = True
        for value_low, value_high in value_dic.items():
            if value_low < value and value_high > value:
                flag_ok = False
                break
            else:
                pass
        if flag_ok:
            for one in values_low:
                if one > value:
                    total += (one - value - 1)
                    break
                else:
                    pass
        else:
            pass
    
    if value < 4294967295:
        total += (4294967295 - value)
    return total
    
if __name__ == '__main__':
    #*************part1*************************    
    list = read_input('input.txt')
    # print order_ips(list)
    #*************part2*************************      
    print total_ips(list)
    
    print '\n'
    print 'All done baby!!'