# 6.11 in Elements of Programming Interviews in Python (Sep 15, 2016)
# write a program which takes as input a string s and returns the snakestring
# of s which is written in sinusoidal fashion.

import unittest

# time complexity O(len(s))
# space complexity O(len(s))

def snakestring(s):
    i = 1
    j = 0
    m = 3
    s_new = []

    while i < len(s):
        s_new.append(s[i])
        i += 4
    while j < len(s):
        s_new.append(s[j])
        j += 2
    while m < len(s):
        s_new.append(s[m])
        m += 4

    return "".join(s_new)

class Test(unittest.TestCase):
    def test_snakestring(self):
        self.assertEqual(snakestring("Hello World!"), 'e lHloWrdlo!');

if __name__ == "__main__":
    unittest.main()
