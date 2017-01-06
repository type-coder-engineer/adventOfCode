# coding: utf
import copy

def read_input(filename):
    data = []
    target = open(filename, 'r')
    for line in target:
        mystring = ''
        line = line.strip('\n')
        for letter in line:
            mystring += letter
        data.append(mystring)
    return data

def get_code(input):
    code = ''
    for i in range(0,8):
        mystring = ''
        for one in input:
            mystring += one[i]
        # letter = most_frequency(mystring) # part1
        letter = least_frequency(mystring) # part2
        code += letter
    return code
        
def most_frequency(string):
    mydic = {}
    for one in string:
        if one in mydic.keys():
            mydic[one] += 1
        else:
            mydic[one] = 1
    list_values = copy.copy(mydic.values())
    list_values.sort()
    for key, value in mydic.items():
        if value == list_values[-1]:
            return key
            
def least_frequency(string):
    mydic = {}
    for one in string:
        if one in mydic.keys():
            mydic[one] += 1
        else:
            mydic[one] = 1
    list_values = copy.copy(mydic.values())
    list_values.sort()
    for key, value in mydic.items():
        if value == list_values[0]:
            return key            

if __name__ == '__main__':
    #*************part1*************************    
    # input = read_input('input.txt')
    # print get_code(input)
    #*************part2*************************      
    input = read_input('input.txt')
    print get_code(input)
    
    print '\n'
    print 'All done baby!!'