# coding:utf-8

def choose_time(list):
    right_time = -1
    while(1):
        right_time += 1
        flag_ok = True
        for i in range(0, len(list)):
            time = right_time + i + 1
            position = det_position(list[i][0], list[i][1], time)
            # print position
            if position != 0:
                flag_ok = False
                break
        # raw_input()        
        if flag_ok:
            return right_time
            
def det_position(length, initial, time):
    pos = initial + time
    if pos >= length:
        pos = pos % length
    return pos
    
if __name__ == '__main__':
    #*************part1*************************    
    list = []
    list.append([13,11])
    list.append([5,0])
    list.append([17,11])
    list.append([3,0])
    list.append([7,2])
    list.append([19,17])
    
    #*************part2*************************   
    list.append([11,0]) 
    print choose_time(list)    
    print '\n'
    print 'All done baby!!'