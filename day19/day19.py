# coding: utf-8

def steal_left(input):
    mylist = []
    new = []
    for i in range(0, input):
        mylist.append(i)
    index = -1
    while(len(mylist) > 1):
        index += 1
        # print mylist
        if index % 2 == 0:
            new.append(mylist[index])
        else:
            pass
        if index == len(mylist) - 1:
            # print new
            # raw_input()
            if index % 2 == 0:
                del new[0]
            else:
                pass
            mylist = new
            index = -1
            new = []
            
    return mylist[0]    

def steal_across(input):
    mylist = []
    for i in range(0, input):
        mylist.append(i)
    index = -1
    while(len(mylist) > 1):
        # print len(mylist)
        # print mylist
        # raw_input()
        index += 1
        element = mylist[index]
        # print len(mylist)
        # print det_pos(index + len(mylist)/2, len(mylist))
        if len(mylist) % 2 == 0:
            index_del = det_pos(index + len(mylist)/2, len(mylist))
            del mylist[index_del]
        else:
            index_del = det_pos(index + (len(mylist) - 1)/2, len(mylist))
            del mylist[index_del]
        if index_del < index:
            index = mylist.index(element) # 这样可以得到正在处理的元素在当前list中的位置
        else:
            pass
        if index == len(mylist) - 1:
            index = -1
    print '**********************'
    return (mylist[0] + 1)
    
def det_pos(index, length):
    if index < length:
        pass
    else:
        index -= length
    return index
    
if __name__ == '__main__':
    #*************part1*************************    
    input = 3014603
    # print steal_left(input)
    #*************part2*************************      
    print steal_across(input)
    
    print '\n'
    print 'All done baby!!'