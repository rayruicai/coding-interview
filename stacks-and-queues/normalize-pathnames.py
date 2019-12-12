# 8.4 in Elements of Programming Interviews in Python (Sep 15, 2016)
# write a program which takes a pathname, and returns the shortest
# equivalent pathname.

import unittest

# time complexity O(len(string))
# space complexity O(len(string))

class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        return self.items[-1]

def normalize_pathnames(string):
    # split string with /
    path_lst = string.split('/')
    
    # push each element in the list to stack
    path_lst_short = []
    P = Stack()

    for i in path_lst:
        if i != '' and i != '.':
            if i == '..':
                if P.isEmpty() or P.peek() == '..':
                    P.push(i)
                else:
                    P.pop()
            else:
                P.push(i)

    # pop short pathname
    while not P.isEmpty():
        path_lst_short.insert(0, P.pop())

    # distinguish between absolute and relative pathname
    if path_lst[0] == '':
        if path_lst_short[0] == '..':
            raise ValueError('Path error')
        else:
            return '/' + '/'.join(path_lst_short)
    else:
        return '/'.join(path_lst_short)

class Test(unittest.TestCase):
    def test_normalize_pathnames(self):
        pathname1 = 'scripts//./../scripts/awkscripts/././'
        self.assertEqual(normalize_pathnames(pathname1), 'scripts/awkscripts');
        pathname2 = '/usr/lib/../bin/gcc'
        self.assertEqual(normalize_pathnames(pathname2), '/usr/bin/gcc');
        pathname3 = '/../scripts/awkscripts/././'
        self.assertRaises(ValueError, normalize_pathnames, pathname3)

if __name__ == "__main__":
    unittest.main()
