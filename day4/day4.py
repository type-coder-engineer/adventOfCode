# coding: utf
import copy

def read_input(filename):
    input = []
    for line in open(filename, 'r'):
        line = line.strip('\n')
        line = line.strip(' ')
        line = line.strip(']')
        mediate = line.split('-')
        # string = ''.join(mediate[0:-1]) # part1
        string = ' '.join(mediate[0:-1])
        last_two = mediate[-1].split('[')
        my_hint = [string, int(last_two[0]), last_two[1]]
        input.append(my_hint)
    return input

def det_code(input):
    code = 0
    # ok = 0
    # time = 0
    for one in input:
        # time += 1
        # print one
        code_dic = {}
        for letter in one[0]:
            if letter in code_dic.keys():
                code_dic[letter] += 1
            else:
                code_dic[letter] = 1
                
        five_letters = five_common(code_dic)
        # print five_letters
        # print one[-1]
        if len(one[-1]) != 5:
            raw_input()
        if five_letters == False:
            # print one
            # raw_input()
            continue
        else:
            if five_letters == one[-1]:
                code += one[1]
                # ok += 1
            else:
                pass
    # print ok
    return code
    
def five_common(code_dic):
    string_return = ''
    list_to_choose = copy.copy(code_dic.values())
    list_to_choose.sort()
    if len(list_to_choose) < 5:
        return False
    else:
        mylist = []
        for i in range(1,6):
            mylist.append(list_to_choose[-i])
        # print mylist
        mylist_unique = list(set(mylist)) # 去除重复的元素，因为set中只能有不重复的元素，碉堡了
        mylist_unique.sort()
        mylist_unique.reverse() # 还要再reverse一次，因为list自动按从小到大排列了
        # 操一个很恶心的bug，有一行reverse之后还是没有从大到小排列。。。但是先sort()再reverse()就没问题
        # 不晓得什么情况。。。
        # print mylist_unique
        for one in mylist_unique:
            list_keys = []
            for key, value in code_dic.items():
                if value == one:
                    list_keys.append(key)
            list_keys.sort()
            for one in list_keys:
                # print one
                string_return += one
    # print string_return
    return string_return[0:5]

def det_name(input):
    new_list = []
    for one in input:
        new_one = ''
        for letter in one[0]:
            if letter != ' ':
                new_letter = inverter(letter, one[1])
                new_one += new_letter
            else:
                new_one += ' '
        new_list.append([new_one, one[1]])
    return new_list
    
def inverter(letter, step):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    my_index = alphabet.index(letter)
    move = step % 26
    my_index += move
    if my_index > 25:
        my_index = my_index - 26
    return alphabet[my_index]

def search_key(list):
    key = 'north'
    print key
    for one in list:
        if key in one[0]:
            print one[0]
            print one[1]
    return
    # something funny
# if you search 'sea' as your key word, you will get:
# weaponized scavenger hunt research
# 941
# rampaging projectile flower research
# 135
# weaponized bunny research
# 213
# fuzzy colorful chocolate research
# 577   

if __name__ == '__main__':
    #*************part1*************************    
    # input = read_input('input.txt')
    # print det_code(input)
    #*************part2*************************      
    input = read_input('input.txt')
    # print det_name(input)
    new_list = det_name(input)
    # print new_list
    search_key(new_list)
    print '\n'
    print 'All done baby!!'