# coding: utf
# a script to test day17.py
import day17
# import bfs
from nose.tools import *

def test_part1():
    test1 = 'ihgpwlah'
    test2 = 'kglvqrro'
    test3 = 'ulqzkmiv'
    assert_equal(day17.shortest_path(day17.search_path(test1, [0,0], [])), 'DDRRRD')
    assert_equal(day17.shortest_path(day17.search_path(test2, [0,0], [])), 'DDUDRLRRUDRD')
    assert_equal(day17.shortest_path(day17.search_path(test3, [0,0], [])), 'DRURDRUDDLLDLUURRDULRLDUUDDDRR')
    
def test_part2():
    test1 = 'ihgpwlah'
    test2 = 'kglvqrro'
    test3 = 'ulqzkmiv'
    assert_equal(day17.longest_path(day17.search_path(test1, [0,0], [])), 370)
    assert_equal(day17.longest_path(day17.search_path(test2, [0,0], [])), 492)
    assert_equal(day17.longest_path(day17.search_path(test3, [0,0], [])), 830)
    
    
if __name__ == '__main__':
    try:
        test_part2()
        print 'All good'
    except AssertionError as e:
        raise
  